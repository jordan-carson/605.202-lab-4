import os
from pathlib import Path

current_path = Path('.').absolute()
root = current_path.parent
data_path = os.path.join(root, "605.202-lab-4", "include", "generated")


def read_files(path, prefix=None):
    return [os.path.join(path, i) for i in os.listdir(path) if os.path.exists(os.path.join(path, i))] if not prefix \
        else [os.path.join(path, p) for p in os.listdir(path) if p.startswith(prefix) and os.path.exists(os.path.join(path, i))]


def read_file(file_path):
    with open(file_path, "r",) as f:
        data = f.read().splitlines()
    return [int(_) for _ in data]


data_files = read_files(data_path)
data_dict = {os.path.basename(file): read_file(file) for file in data_files}
