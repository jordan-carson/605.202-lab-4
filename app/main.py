import argparse
import os
import pathlib
import time

from app.core.models import mergesort, heapsort, quicksort, insertion
from app.core.services.generate_files import create_all


PATH = pathlib.Path(os.getcwd()).absolute().parent


def main():
    parser = argparse.ArgumentParser("Comparing Quicksort and Merge Sort Algorithms")
    parser.add_argument("--sorting_algo", choices=[
        "All", "quicksort vs insertion", 'quicksort', 'mergesort', "natural-mergesort", "heapsort", "insertion"
    ])
    parser.add_argument("--generate-files-apriori", default=True, choices=["True", "False"])

    args = parser.parse_args()

    results = {}

    dico = {
        "quicksort": quicksort.quicksort_iterative,
        "mergesort": mergesort.mergesort, # no
        "heapsort": heapsort.heapsort,
        "insertion": insertion.insertion,
    }

    start = time.time_ns()
    results["args"] = args.__dict__

    results["Start_Time"] = start
    results["Sorting_Algo"] = args.sorting_algo

    # need a function to read the file from the DATA_PATH



    if args.sorting_algo == "All":
        for k, v in dico:







    end = time.time_ns()



    return True


if __name__ == '__main__':
    main()