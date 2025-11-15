echo "=== Проверка обратных зависимостей (test + --reverse) ==="
echo "--- Прямой граф зависимостей ---"
python3 /home/mikhail/PycharmProjects/konfupr2/main.py \
  --package A \
  --repo ../test_repo_stage3/./graph_6.txt \
  --mode test \
  --output result.svg

echo "--- Обратный граф зависимостей ---"
python3 /home/mikhail/PycharmProjects/konfupr2/main.py \
  --package E \
  --repo ../test_repo_stage3/./graph_6.txt \
  --mode test \
  --reverse \
  --output result.svg