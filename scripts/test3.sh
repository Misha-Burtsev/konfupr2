#!/bin/bash
set -e  # выход при ошибке

echo "=== Проверка тестовых графов (этап 3) ==="

# 1. Линейный граф
echo "--- Тест 1: линейный граф ---"
python3 /home/mikhail/PycharmProjects/konfupr2/main.py \
  --package A \
  --repo ../test_repo_stage3/./graph_1.txt \
  --mode test \
  --output result.svg

# 2. Разветвлённые зависимости
echo "--- Тест 2: ветвление ---"
python3 /home/mikhail/PycharmProjects/konfupr2/main.py \
  --package A \
  --repo ../test_repo_stage3/./graph_2.txt \
  --mode test \
  --output result.svg

# 3. Циклические зависимости
echo "--- Тест 3: цикл ---"
python3 /home/mikhail/PycharmProjects/konfupr2/main.py \
  --package A \
  --repo ../test_repo_stage3/./graph_3.txt \
  --mode test \
  --output result.svg

# 4. Несвязный граф
echo "--- Тест 4: несвязный граф ---"
python3 /home/mikhail/PycharmProjects/konfupr2/main.py \
  --package A \
  --repo ../test_repo_stage3/./graph_4.txt \
  --mode test \
  --output result.svg

# 5. Пустые зависимости
echo "--- Тест 5: пустые зависимости ---"
python3 /home/mikhail/PycharmProjects/konfupr2/main.py \
  --package A \
  --repo ../test_repo_stage3/./graph_5.txt \
  --mode test \
  --output result.svg

# 6. Граф побольше
echo "--- Тест 6: граф побольше ---"
python3 /home/mikhail/PycharmProjects/konfupr2/main.py \
  --package A \
  --repo ../test_repo_stage3/./graph_6.txt \
  --mode test \
  --output result.svg