#!/bin/bash
set -e  # выход при первой же ошибке

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="${SCRIPT_DIR}/.."

echo "=== 5.1: Визуализация простого тестового графа (graph_1.txt, mode=test) ==="
python3 "${PROJECT_ROOT}/main.py" \
  --package A \
  --repo "${PROJECT_ROOT}/test_repo_stage3/graph_1.txt" \
  --mode test \
  --output "${PROJECT_ROOT}/test_repo_stage3/graph_1.svg"

echo "=== 5.2: Визуализация графа с более сложными зависимостями (graph_6.txt, mode=test) ==="
python3 "${PROJECT_ROOT}/main.py" \
  --package A \
  --repo "${PROJECT_ROOT}/test_repo_stage3/graph_6.txt" \
  --mode test \
  --output "${PROJECT_ROOT}/test_repo_stage3/graph_6.svg"

echo "=== 5.3: Визуализация зависимостей локального npm-проекта (demo_local_repo, mode=local) ==="
python3 "${PROJECT_ROOT}/main.py" \
  --package testpkg \
  --repo "${PROJECT_ROOT}/demo_local_repo" \
  --mode local \
  --output "${PROJECT_ROOT}/demo_local_repo/deps.svg"

echo "=== Тесты этапа 5 завершены ==="
