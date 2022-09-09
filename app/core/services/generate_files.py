import logging
import os.path

from app.core.utils import file_utils as futil, logger
import itertools

from pathlib import Path

# logger = logging.getLogger("lab4")

logger = logger.logger


def generate_files(file_type: str, file_size: int) -> bool:
    """
    File type can be asc, dup, ran, rev -
    File Size can be 50, 500, 1000, 2000, 5000, 10000, 20000
    :param file_type:
    :return: file_name
    """
    if file_type.lower() not in ['asc', 'dup', 'ran', 'rev']:
        raise ValueError('file_type is not correct, Check again and regenerate the files.')

    if file_size not in [50, 500, 1000, 2000, 5000, 10000, 20000]:
        raise ValueError('file_size is not correct. Check again and regenerate the files.')

    data = {
        'asc': futil.create_asc, 'dup': futil.create_dup, 'ran': futil.create_random, 'rev': futil.create_rev
    }[file_type.lower()]

    file_name = f"{futil.DATA_PATH}/generated/{file_type.lower()}_{file_size}.txt"
    futil.writer(file_name, data(file_size)) if not file_type == "ran" \
        else futil.writer(file_name, data(file_size, 0, file_size))

    return os.path.exists(file_name)


def create_all():
    logging.info("")
    sizes = [50, 500, 1000, 2000, 5000, 10000, 20000]
    _types = ['asc', 'dup', 'ran', 'rev']

    for _type, _size in itertools.product(_types, sizes,):
        logger.info(f"generating file: type:{_type} with size: {_size}")
        generate_files(_type, _size)

    logger.info("All files generated.")

    return


if __name__ == '__main__':
    create_all()
