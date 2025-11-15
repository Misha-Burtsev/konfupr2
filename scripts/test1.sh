#!/bin/bash
# test_depgraph.sh — демонстрация обработки ошибок

echo "=== Тест 1: все параметры корректны (local) ==="
python3 ../main.py --package demo --repo ./ --mode local --output graph.png
echo

echo "=== Тест 2: все параметры корректны (remote) ==="
python3 ../main.py --package demo --repo https://github/repo --mode remote --output graph.svg
echo

echo "=== Тест 3: отсутствует параметр package ==="
python3 ../main.py --repo ./ --mode local --output graph.png
echo

echo "=== Тест 4: неверный путь при local ==="
python3 ../main.py --package demo --repo ./no_such_dir --mode local --output graph.png
echo

echo "=== Тест 5: неверный repo при remote ==="
python3 ../main.py --package demo --repo ./local_path --mode remote --output graph.png
echo

echo "=== Тест 6: неверное расширение выходного файла ==="
python3 ../main.py --package demo --repo ./ --mode local --output graph.txt
echo

echo "=== Тест 7: неправильный режим ==="
python3 ../main.py --package demo --repo ./ --mode invalid --output graph.png
echo