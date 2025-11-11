import argparse
import os
import sys
import json # Для парсинга (чтения) JSON-файлов
from urllib.parse import urlparse
import urllib.request # Для выполнения веб-запросов (скачивания файла по URL)
from collections import deque # Для реализации обхода графа (BFS)

# ---------------- Аргументы командной строки ---------------- #
parser = argparse.ArgumentParser()
parser.add_argument("--package", required=True)
parser.add_argument("--repo", required=True)
parser.add_argument("--mode", required=True, choices=["local", "remote", "test"]) # Добавлен режим test
parser.add_argument("--output", required=True)
args = parser.parse_args()

# Проверяет, является ли строка корректным http/https URL
def is_url(s: str) -> bool:
    parsed = urlparse(s)
    return parsed.scheme in ("http", "https") and bool(parsed.netloc)

# ---------------- Проверка параметров (этап 1) ---------------- #

if not args.package.strip():
    sys.exit("Ошибка: пустое имя пакета")

if not args.repo.strip():
    sys.exit("Ошибка: пустой путь/URL репозитория")

if args.mode == "local":
    # Для local ожидаем путь к папке
    if is_url(args.repo):
        sys.exit("Ошибка: для режима local repo должен быть путём")
    if not os.path.exists(args.repo):
        sys.exit("Ошибка: путь не найден")
elif args.mode == "remote":
    # Для remote ожидаем сетевой URL
    if not is_url(args.repo):
        sys.exit("Ошибка: для режима remote repo должен быть URL")
else:
    # Для test ожидаем путь к файлу с тестовым графом
    if not os.path.isfile(args.repo):
        sys.exit("Ошибка: файл тестового репозитория не найден")

if not args.output.strip():
    sys.exit("Ошибка: пустое имя выходного файла")
if not args.output.endswith((".png", ".svg", ".pdf")):
    sys.exit("Ошибка: output должен иметь расширение .png/.svg/.pdf")

# ---------------- Этап 2: чтение package.json ---------------- #
def load_package_json(repo: str, mode: str):            # Возвращает содержимое package.json в виде словаря.

    if mode == "local":
        path = os.path.join(repo, "package.json")       # Собираем полный путь к файлу package.json
        if not os.path.isfile(path):                    # Проверяем, существует ли такой файл
            sys.exit("Ошибка: package.json не найден в указанном каталоге")
        with open(path, "r", encoding="utf-8") as f:    # "r" только для чтения
            return json.load(f)                         # Читаем содержимое файла и сразу парсим его из JSON в словарь Python


    else:
        url = repo.rstrip("/")
        if "github.com/" not in url:
            sys.exit("Ошибка: в режиме remote поддерживаются только GitHub-репозитории")

        tail = url.split("github.com/", 1)[1]
        raw_url = f"https://raw.githubusercontent.com/{tail}/master/package.json"
        try:
            with urllib.request.urlopen(raw_url) as resp:
                data = resp.read().decode("utf-8")          # Читаем сырые байты (resp.read()) и декодируем их в текст (UTF-8)
        except Exception as e:
            sys.exit(f"Ошибка: не удалось загрузить package.json по URL {raw_url}: {e}")
            # Пытаемся распарсить полученный текст как JSON
        try:
            # json.loads() используется для парсинга строки (s = string)
            # в отличие от json.load(), который парсит из файла
            return json.loads(data)
        except json.JSONDecodeError:
            sys.exit("Ошибка: неверный JSON в package.json")

# ---------------- Этап 3: тестовый граф и обход BFS ---------------- #
def load_test_graph(path: str):                         # Загружает тестовый граф из файла
    graph = {}
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):        # Пропускаем пустые строки и комментарии
                continue
            if ":" not in line:
                sys.exit(f"Ошибка: неверный формат строки: {line}")
            pkg, deps_str = line.split(":", 1)
            deps = deps_str.strip().split() if deps_str.strip() else []       #  "  B C D  " -> ["B", "C", "D"]
            graph[pkg.strip()] = deps                   # Формат: {'A': ['B', 'C']}
    return graph

def bfs(graph: dict, start: str):                       # Реализация обхода в ширину (BFS)
    if start not in graph:
        sys.exit(f"Ошибка: стартовый пакет {start} отсутствует в графе")
    visited = set([start])
    order = []                                          # Итоговый список
    q = deque([start])
    while q:
        v = q.popleft()
        order.append(v)                                 # Итоговый список
        for neigh in graph.get(v, []):                  # Смотрим соседей для v
            if neigh not in visited:
                visited.add(neigh)
                q.append(neigh)
    return order                                        # Возвращает порядок обхода вершин

# ---------------- Основная логика ---------------- #

if args.mode == "test":                                 # Тестовый режим
    graph = load_test_graph(args.repo)                  # Загружаем граф из текстового файла
    order = bfs(graph, args.package)                    # Обход графа начиная с указанного пакета
    print("Порядок обхода графа (BFS):")
    print(" ".join(order))

else:                                                   # Режимы local и remote
    # Загружаем JSON-файл и извлекаем зависимости
    pkg = load_package_json(args.repo, args.mode)       # Загрузка
    deps = pkg.get("dependencies") or {}                # Deps всегда будет словарем.

    # Проверка формата dependencies. Если вдруг не словарь, то выпадет ошибка
    if not isinstance(deps, dict):
        sys.exit("Ошибка: поле dependencies в package.json имеет неверный формат")

    # ---------------- Вывод прямых зависимостей ---------------- #
    print("Прямые зависимости пакета:")
    if not deps:
        print("(нет зависимостей)")
    else:
        for name, version in deps.items():
            print(f"{name} {version}")