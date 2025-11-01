import argparse
import os
import sys
from urllib.parse import urlparse

parser = argparse.ArgumentParser()
parser.add_argument("--package", required=True)
parser.add_argument("--repo", required=True)
parser.add_argument("--mode", required=True, choices=["local", "remote"])
parser.add_argument("--output", required=True)
args = parser.parse_args()

def is_url(s):
    return urlparse(s).scheme in ("http", "https")

if not args.package.strip():
    sys.exit("Ошибка: пустое имя пакета")

if args.mode == "local":
    if is_url(args.repo):
        sys.exit("Ошибка: для режима local repo должен быть путём")
    if not os.path.exists(args.repo):
        sys.exit("Ошибка: путь не найден")
else:
    if not is_url(args.repo):
        sys.exit("Ошибка: для режима remote repo должен быть URL")

if not args.output.endswith((".png", ".svg", ".pdf")):
    sys.exit("Ошибка: output должен иметь расширение .png/.svg/.pdf")

print(f"package = {args.package}")
print(f"repo = {args.repo}")
print(f"mode = {args.mode}")
print(f"output = {args.output}")
