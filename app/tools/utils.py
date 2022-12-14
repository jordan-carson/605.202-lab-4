import random
# from app.core.tools import Je
import time


def print_array_as_string(array):
    return ", ".join(array)


def median(array, left, right):
    bound = max(right - left, left - right)
    mid = ((bound - (bound % 2)) / 2) + left
    if array[left] > array[mid]:
        swap(array, left, mid)

    if array[left] > array[right]:
        swap(array, left, right)

    if array[mid] > array[right]:
        swap(array, mid, right)

    swap(array, left, mid)

    return


def partition(array, left_idx, right_idx, include_median=False):
    if len(array) == 0 or not isinstance(array, list):
        return array

    if include_median:
        median(array, left_idx, right_idx)

    pivot = array[right_idx]

    tmp_idx = left_idx - 1

    for j in range(right_idx - 1):
        if array[j] <= pivot:
            tmp_idx += 1
            swap(array, tmp_idx, j)

    swap(array, tmp_idx + 1, right_idx)
    return tmp_idx + 1


# def swap(array, index1, index2, ret_val=None):
#     array[index1], array[index2] = array[index2], array[index1]
#     return None if not ret_val else array


def generate_data(size, reverse=False, shuffle_output=False):
    res = list()
    for i in range(0, size):
        res.append(i)
    # reverse
    if reverse:
        res.reverse()
    if shuffle_output:
        random.shuffle(res)
    return res


def read_input_file(filename):
    return open(filename, "r").read().split('\n')


def create_output_file(filename: str, data: list):
    with open(filename, "w") as file_out:
        file_out.writelines(data)


def swap_positions(arr, p1, p2):
    arr[p1], arr[p2] = arr[p2], arr[p1]
    return arr


def swap(arr, a, b):
    arr[b], arr[a] = arr[a], arr[b]


def partition_quicksort(array, low, high,):

    pivot = array[high]

    b = low
    for a in range(low, high):
        if array[a] < pivot:
            swap(array, a, b)
            b += 1
    swap(array, high, b)
    return b


def concat(before, pivot, after):
    new = []
    for items in before:
        new.append(items)
    new = [item for item in before]
    new.append(pivot)
    for things in after:
        new.append(things)
    return new


def concat_comprehension(before, pivot, after):
    return [_ for _ in before] + [pivot] + [_ for _ in after]


def human_readable_time(unix_epoch_nanoseconds: int) -> str:
    from datetime import datetime
    dt = datetime.fromtimestamp(unix_epoch_nanoseconds // 1000000000)
    nano = "." + str(int(unix_epoch_nanoseconds % 1000000000)).zfill(9)
    return dt.strftime('%Y-%m-%d %H:%M:%S') + nano
