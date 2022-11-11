# from app.tools.logger import logger
import itertools
import os.path

from app.tools import file_utils as futil


def generate_files(file_type: str, file_size: int) -> bool:
    """
    File type can be asc, dup, ran, rev -
    File Size can be 50, 500, 1000, 2000, 5000, 10000, 20000
    :param file_size:
    :param file_type:
    :return: file_name
    """
    if file_type.lower() not in ['asc', 'dup', 'ran', 'rev']:
        raise ValueError('file_type is not correct, Check again and regenerate the data.')

    if file_size not in [50, 500, 1000, 2000, 5000, 10000, 20000]:
        raise ValueError('file_size is not correct. Check again and regenerate the data.')

    data = {
        'asc': futil.create_asc, 'dup': futil.create_dup, 'ran': futil.create_random, 'rev': futil.create_rev
    }[file_type.lower()]

    file_name = f"{futil.DATA_PATH}/data/{file_type.lower()}_{file_size}.txt"
    futil.writer(file_name, data(file_size)) if not file_type == "ran" \
        else futil.writer(file_name, data(file_size, 0, file_size))
    print(f"Generating file: {os.path.basename(file_name)} Path: {file_name} Type:{file_type} Size: {file_size}")
    return os.path.exists(file_name)


def create_all():
    sizes = [50, 500, 1000, 2000, 5000, 10000, 20000]
    _types = ['asc', 'dup', 'ran', 'rev']

    for _type, _size in itertools.product(_types, sizes,):
        generate_files(_type, _size)

    print("All data data.")

    return
