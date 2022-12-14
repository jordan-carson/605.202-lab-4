import os
import random
from pathlib import Path

SEED: int = os.getenv("SEED", 18)
DATA_PATH = Path("/include").absolute()
# PATH = Path(os.getcwd( = / )).absolute().parent


def create_asc(n):
    return [i for i in range(1, n+1)]


def create_random(n, low, high):
    if not high:
        high = n

    if not low:
        low = 0
    return random.sample(range(low, high), n)


def create_rev(n):
    asc = create_asc(n)
    asc.reverse()
    return asc


def create_dup(n):
    """
    Divides n by 2 - creates a list of n//2 then another duplicated list randomized of the same numbers.
    """
    return create_random(int(n // 2), int(n // 2), n) + create_random(int(n // 2), int(n // 2), n)


def writer(filename, inp: list):
    with open(filename, 'w') as f:
        for i in inp:
            f.write("%s\n" % i)
    return True


def read_files(path, prefix=None):
    return [os.path.join(path, p) for p in os.listdir(path)] if not prefix \
        else [os.path.join(path, p) for p in os.listdir(path) if p.startswith(prefix)]


def read_file(file_path):
    res = dict()
    with open(file_path, "r",) as f:
        res["data"] = f.readlines()
    return res
