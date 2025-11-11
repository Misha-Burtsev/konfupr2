#!/bin/bash
set -e  # выход при ошибке

# 1. Проверка локального режима
echo "=== Проверка режима local ==="
python3 /home/mikhail/PycharmProjects/konfupr2/main.py \
  --package testpkg \
  --repo ../demo_local_repo \
  --mode local \
  --output result.svg

# 2. Проверка удалённого режима (GitHub)
echo "=== Проверка режима remote ==="
python3 /home/mikhail/PycharmProjects/konfupr2/main.py \
  --package express \
  --repo https://github.com/expressjs/express \
  --mode remote \
  --output result.svg