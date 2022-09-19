import argparse
import os
import pathlib
import time


from app.core.models import mergesort, heapsort, quicksort, insertion
from app.core.services.generate_files import create_all
from app.constants import data_path, data_files, data_dict
from app.core.utils.logger import logger
from app.core.exceptions import IncorrectSortingAlgoError, QuicksortRecursionError, QuicksortEmptyArrayException

PATH = pathlib.Path(os.getcwd()).absolute().parent


def read_files(path, prefix=None):
    return [os.path.join(path, p) for p in os.listdir(path)] if not prefix \
        else [os.path.join(path, p) for p in os.listdir(path) if p.startswith(prefix)]


def read_file(file_path):
    res = dict()
    with open(file_path, "r",) as f:
        res["data"] = f.readlines()
    return res


def main():
    parser = argparse.ArgumentParser("Comparing Quicksort and Merge Sort Algorithms")
    parser.add_argument("--sorting_algo", choices=[
        "All", "quicksort vs insertion", 'quicksort', 'mergesort', "natural-mergesort", "heapsort", "insertion"
    ])
    parser.add_argument("--generate-files-apriori", default=True, choices=["True", "False"])
    parser.add_argument("--file-type", default="all", choices=["all", 'asc', 'ran', 'dup', 'rev'])

    args = parser.parse_args()

    dico = {
        # "quicksort_recursive": quicksort.quicksort_recursive,
        "quicksort": quicksort.quicksort_recursive2, # works perfectly
        # "mergesort": mergesort.mergesort, # no
        # "heapsort": heapsort.heapsort,
        # "insertion": insertion.insertion, # good
    }

    results = dict()
    for name, algo in dico.items():
        start = time.time_ns()
        results["algo_name"] = name
        results["algo_start"] = start
        file_res = {}
        for i, (file, data) in enumerate(data_dict.items()):
            try:
                _start_ns = time.time_ns()
                _start_secs = time.time()
                res = algo(data)
                _end_ns = time.time_ns()
                _end_secs = time.time()
                total_time_ns = _end_ns - _start_ns
                total_time_secs = _end_secs - _start_secs
                if i == 0:
                    logger.info(f"Name: {name}, File: {file}, Time_ns: {round(total_time_ns) * 1e+9}, "
                                f"Time_secs: {round(total_time_secs)}", f"Data: {min(data)}, {max(data)}, "
                                f"{type(data)}, {len(data)}")

                file_res[file] = {
                    "Name": name, "first_item": data[0], "last_item": data[-1],
                    "length": len(data), "result_type": type(res), "res_first_item": res[0],
                    "res_last_item": res[-1], "finished": True if res[0] < res[-1] else False,
                    "algo_start": {'ns': _start_ns, 'secs': _start_secs},
                    "algo_end": {'ns': _start_ns, 'secs': _start_secs},
                    "algo_time_diff": {"ns": total_time_ns, "secs": total_time_secs},
                }
            except Exception as err:
                logger.exception(str(err))
                logger.exception(f"Name: {name}, File: {file}")
                pass
            results[file] = file_res

    from pprint import pprint
    pprint(results)
    return results


if __name__ == '__main__':
    logger.info("INITIALIZING")
    main()