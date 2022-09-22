import argparse
import os
import pathlib
import time

import pandas as pd
from app.core.models import natural_merge_sort, quicksort
from app.core.services.generate_files import create_all
from app.constants import file_path, data_dict, filter_data_dict
from app.core.utils.logger import logger
from app.core.exceptions import IncorrectConfigurationError
import datetime


PATH = pathlib.Path(os.getcwd()).absolute()
print(PATH)


def main():
    logger.info(f"Initializing Lab4: Data Path {file_path}")
    parser = argparse.ArgumentParser("Comparing Quicksort and Merge Sort Algorithms")
    parser.add_argument("--sorting_algo", choices=["All", 'quicksort', 'mergesort', "natural-mergesort", ])
    parser.add_argument("--generate_files", default=False, choices=[True, False])
    parser.add_argument("--input_file_type", default="all", choices=["all", 'asc', 'ran', 'dup', 'rev'])

    args = parser.parse_args()

    if args.generate_files:
        create_all()

    if args.input_file_type in ['asc', 'ran', 'dup', 'rev']:
        flt_data_dict = filter_data_dict(args.input_file_type)
        if not flt_data_dict:
            _data_dict = data_dict
        else:
            _data_dict = data_dict

    dico = {
        "quicksort": quicksort.quicksort_recursive2, # works perfectly
        "mergesort": natural_merge_sort.recursive_merge_sort, # in test mode
        # "insertion": insertion.insertion, # good
        # "mergesort": mergesort.mergesort, # no
        # "heapsort": heapsort.heapsort,
    }

    # if idx == 0:
    #     logger.info(f"Name: {name}, File: {file}, Time_ns: {round(total_time_ns) * 1e+9}, "
    #                 f"Time_secs: {round(total_time_secs)}", f"Data: {min(data)}, {max(data)}, "
    #                                                         f"{type(data)}, {len(data)}")

    results = list()
    algo_res = dict()
    algos = list()
    for i, (name, algo) in enumerate(dico.items(), start=1):
        algo_res["algo_name"] = name
        algo_start = datetime.datetime.utcnow()
        for idx, (file, data) in enumerate(data_dict.items(), start=1):
            logger.info(f"File: {file}, Data: {len(data)} file_output_name:{str(file).split('.')[0]}_result.txt")
            try:
                _start_time = time.time()
                _start_secs = datetime.datetime.utcnow()
                res = algo(data)
                _end_time = time.time()
                _end_secs = datetime.datetime.utcnow()

                tmp_res = \
                    {
                        "algo_nbr": i,
                        "iteration_number": idx,
                        "data_file": file,
                        "sorting_algo": name,
                        "length": len(data),
                        "result_type": type(res),
                        "res_first_item": res[0],
                        "res_last_item": res[-1],
                        "completed?": "True" if res[0] < res[-1] else "False",
                        "first_item": data[0],
                        "last_item": data[-1],
                        "algo_start_ns": _start_time,
                        "algo_end_ns": _end_time,
                        "algo_time_diff_secs": str(datetime.timedelta(seconds=(_end_time - _start_time))),
                        'algo_start_secs': _start_secs,
                        'algo_end_secs': _start_secs,
                        "total_seconds": (_end_secs - _start_secs).total_seconds(),
                    }
                results.append(pd.DataFrame.from_records(tmp_res, index=[len(tmp_res.keys())]))
                with open(str(file).split(".")[0] + "_result.txt", 'w') as file_out:
                    file_out.write(res)
            except Exception as err:
                logger.exception(str(err))
                logger.exception(f"Name: {name}, File: {file}")
                raise IncorrectConfigurationError(f"Incorrect configuration for {name}, {file}.")
        algo_res['total_seconds'] = (datetime.datetime.utcnow() - algo_start).total_seconds()
        algos.append(
            pd.DataFrame.from_records(algo_res, index=[len(algo_res.keys())])
        )

    final_df = pd.concat(results)
    algo_df = pd.concat(algos)

    logger.info(final_df.head())
    logger.info(algo_df.head(len(algo_res.keys())))
    final_df.to_csv("/Users/jordancarson/Projects/605.202-lab-4/include/out/FinalOutput.csv")
    return final_df, algo_df


if __name__ == '__main__':
    logger.info("INITIALIZING")
    main()