import argparse
import os
import sys
import time
from functools import lru_cache
from pathlib import Path

import pandas as pd

from app.models import natural_merge_sort, quicksort
from app.tools.file_utils import writer
from app.tools.generate_files import create_all
from app.tools.utils import human_readable_time

sys.setrecursionlimit(20000)
PATH = Path(".").absolute()

file_path = PATH / "include" / "data"


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


def main():
    print(f"Initializing Lab4: Current Directory {PATH} / Data Path {file_path}.")
    parser = argparse.ArgumentParser("Comparing Quicksort and Merge Sort Algorithms")
    # parser.add_argument("--sorting_algo", choices=['quicksort', 'mergesort',])
    parser.add_argument("--generate_files", default=False, choices=[True, False])

    # parser.add_argument("--input_file_type", default="all", choices=["all", 'asc', 'ran', 'dup', 'rev'])
    # if args.input_file_type in ['asc', 'ran', 'dup', 'rev']:
    #     flt_data_dict = filter_data_dict(args.input_file_type)
    #     if not flt_data_dict:
    #         _data_dict = data_dict
    #     else:
    #         _data_dict = data_dict
    # data_dict =

    args = parser.parse_args()

    if args.generate_files == True:
        create_all()

    dico = {
        "quicksort_first": quicksort.hybrid_quicksort_first,
        "quicksort_50": quicksort.hybrid_quicksort_50,
        "quicksort_100": quicksort.hybrid_quicksort_100,
        "quicksort_median_of_three": quicksort.quicksort_median_of_three,
        "mergesort": natural_merge_sort.recursive_merge_sort,
    }
    output_path = Path(".").absolute() / "output"
    os.makedirs(output_path, exist_ok=True)

    meta_data = dict()
    dataframe_results = list()
    for name, algo in dico.items():
        meta_data[name] = dict()
        for idx, (file, data) in enumerate(data_dict.items(), start=1):
            meta_data[name][file] = dict()
            output_name = file.split('.')[0]

            start = time.time_ns()

            # run the algo
            if name == "mergesort":
                result = algo(data)
                meta_data[name][file]["result_len"] = len(result)
                writer(output_path / f"{output_name}_out.txt", result)
            elif name == "quicksort_median_of_three":
                result = algo(data, )
                meta_data[name][file]["result_len"] = len(result)
                writer(output_path / f"{output_name}_out.txt", result)
            else:
                algo(data, 0, len(data) - 1)
                meta_data[name][file]["result_len"] = len(data)
                writer(output_path / f"{output_name}_out.txt", data)

            end = time.time_ns()
            meta_data[name][file]["total_time"] = time.time_ns() - start
            print(f"Running Algo - {name} on file {file}, size of data {len(data)}, total time ns {end - start}.")
            dataframe_results.append({
                "algo_name": name, "file_name": file, "total_time_ns": end - start,
                "start": human_readable_time(start), "end": human_readable_time(end),
            })

    df = pd.DataFrame(dataframe_results)
    df.to_csv("full_results.csv")
    print(df.head())


if __name__ == '__main__':
    main()
