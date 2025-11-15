# Анализ и визуализация зависимостей (Практическая работа №2)

Приложение выполняет анализ зависимостей npm-пакетов и визуализирует их
в виде графов.\
Поддерживаются режимы **local**, **remote**, **test**. Реализованы этапы
1--5.

## 1. Структура проекта

    main.py
    demo_local_repo/
    test_repo_stage3/
    scripts/

## 2. Требования

Для работы визуализации необходимо установить утилиту **d2**:

    curl -fsSL https://d2lang.com/install.sh | sh
    export PATH="$HOME/.local/bin:$PATH"

## 3. Формат запуска

    python3 main.py --package <имя> --repo <путь/URL> --mode <режим> --output <файл.svg> [--reverse]

### Аргументы

  Параметр    Описание
  ----------- -------------------------------------------------------
  --package   Имя анализируемого пакета\
  --repo      Путь к локальному каталогу, test-файлу или URL GitHub\
  --mode      local, remote, test\
  --output    Имя выходного .svg файла\
  --reverse   Вывод обратных зависимостей (только test)

# Этап 1 Чтение параметров

Реализовано: обработка аргументов, проверки формата, сообщения об
ошибках.

# Этап 2 Получение прямых зависимостей

### local

    python3 main.py --package testpkg --repo demo_local_repo --mode local --output deps.svg

### remote

    python3 main.py --package axios --repo https://github.com/axios/axios --mode remote --output axios.svg

# Этап 3 BFS (test)

    A: B C
    B: D
    C:
    D:

Пример:

    python3 main.py --package A --repo test_repo_stage3/graph_1.txt --mode test --output out.svg

# Этап 4 Обратные зависимости

    python3 main.py --package B --repo test_repo_stage3/graph_4_cycle.txt --mode test --reverse --output out.svg

# Этап 5 Визуализация (D2 → SVG)

Примеры:

    python3 main.py --package A --repo test_repo_stage3/graph_6.txt --mode test --output graph_6.svg
    python3 main.py --package testpkg --repo demo_local_repo --mode local --output deps.svg

## Скрипты

    ./scripts/test5.sh

# Итог

Приложение реализует все этапы практической работы.
