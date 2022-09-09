from typing import Union
from uuid import uuid4


def create_file_name(start, stop):
    return f"input_file_[{start}_{stop}].txt"


def number_generator(start, stop):
    for i in range(start, stop):
        yield i


# def create_nbr_list(start, stop, ): #output_type: Union[str, list]):
#
#     file_name = create_file_name(start, stop)
#
#     # if isinstance(output_type, str):
#
#
#     outfile = open(file_name, "w", encoding="UTF-8")
#
#
#     for i in number_generator(start, stop):
#         outfile.write(i)
#
#
#


if __name__ == '__main__':
    for i in (number_generator(1, 10)):
        print(i)






