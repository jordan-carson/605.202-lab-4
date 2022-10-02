import logging
import os
from pathlib import Path, PosixPath

current_path = Path(r"/Users/jordancarson/Projects/605.202-lab-4").absolute()     # /Users/jordancarson/Projects/605.202-lab-4
root = current_path
if isinstance(root, PosixPath):
    file_path = os.path.join(root, "include", )
    data_path = os.path.join(file_path, "generated", )
    output_path = os.path.join(file_path, "output", )
# if root != "/Users/jordancarson/Projects/605.202-lab-4":
#     data_path = os.path.join(root, "605.202-lab-4", "include", "generated")
#     output_path = os.path.join(root, "605.202-lab-4", "include", "output")
else:
    file_path = os.path.join(root, "include", )
    data_path = os.path.join(file_path, "generated", )
    output_path = os.path.join(file_path, "output", )


def read_files(path, prefix=None):
    return [os.path.join(path, i) for i in os.listdir(path) if os.path.exists(os.path.join(path, i))] if not prefix \
        else [os.path.join(path, p) for p in os.listdir(path) if p.startswith(prefix) and os.path.exists(os.path.join(path, i))]


def read_file(path):
    with open(path, "r", ) as f:
        data = f.read().splitlines()
    return [int(_) for _ in data]


data_files = read_files(file_path)
data_dict = {os.path.basename(file): read_file(file) for file in data_files}


def filter_data_dict(prefix: str):
    return {
        k: v for k, v in data_dict.items() if k.startswith(prefix) or prefix in k
    }


logging.info(f"Data Path: {file_path}")