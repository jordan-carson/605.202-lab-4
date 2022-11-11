__doc__ = """
•	Select the first item of the partition as the pivot. Treat partitions of size one and two as stopping cases.
•	Same pivot selection. For a partition of size 100 or less, use an insertion sort to finish.
•	Same pivot selection. For a partition of size 50 or less, use an insertion sort to finish.
•	Select the median-of-three as the pivot. Treat partitions of size one and two as stopping cases.
"""

import random

from app.models.insertion import insertion_sort_hybrid


def median_of_three(array, low, high):
    mid = (low + high - 1) // 2
    a, b, c = array[low], array[mid], array[high - 1]
    if a <= b <= c:
        return b, mid
    if c <= b <= a:
        return b, mid
    if a <= c <= b:
        return c, high - 1
    if b <= c <= a:
        return c, high - 1
    return a, low


def partition_first(array, low, high):
    pivot = array[low]
    i = low + 1
    for j in range(low + 1, high):
        if array[j] < pivot:
            array[j], array[i] = array[i], array[j]
            i += 1
    array[low], array[i - 1] = array[i - 1], array[low]
    return i - 1


def partition(arr, low, high):
    pivot = arr[high]
    j = low
    for i in range(low, high):
        if arr[i] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    arr[j], arr[high] = arr[high], arr[j]
    return j


def hybrid_quicksort_100(arr, low, high, stopping_case=50):
    while low < high:

        if high - low + 1 < stopping_case:
            insertion_sort_hybrid(arr, low, high)
            break

        else:
            pivot = partition(arr, low, high)

            if pivot - low < high - pivot:
                hybrid_quicksort_100(arr, low, pivot - 1)
                low = pivot + 1

            else:
                hybrid_quicksort_100(arr, pivot + 1, high)
                high = pivot - 1


def hybrid_quicksort_50(arr, low, high, stopping_case=50):
    while low < high:
        if high - low + 1 < stopping_case:
            insertion_sort_hybrid(arr, low, high)
            break

        else:
            pivot = partition(arr, low, high)

            if pivot - low < high - pivot:
                hybrid_quicksort_50(arr, low, pivot - 1)
                low = pivot + 1

            else:
                hybrid_quicksort_50(arr, pivot + 1, high)
                high = pivot - 1


def hybrid_quicksort_first(arr, low, high, ):
    # if len(arr) in [1, 2]:
    #     return arr

    while low < high:
        if high - low + 1 < 1:
            insertion_sort_hybrid(arr, low, high)
            break

        if high - low + 1 < 2:
            insertion_sort_hybrid(arr, low, high)
            break

        else:
            pivot = partition_first(arr, low, high)

            if pivot - low < high - pivot:
                hybrid_quicksort_first(arr, low, pivot - 1)
                low = pivot + 1

            else:
                hybrid_quicksort_first(arr, pivot + 1, high)
                high = pivot - 1


def partition_median(array, low, high):
    pivot = median_of_three(array, low, high)
    i = low + 1
    for j in range(low + 1, high):
        if array[j] < pivot:
            array[j], array[i] = array[i], array[j]
            i += 1
    array[low], array[i - 1] = array[i - 1], array[low]
    return i - 1


def middle_index(x):
    """ Returns the index of the middle element of an array """
    if len(x) % 2 == 0:
        middle_index = len(x) // 2 - 1
    else:
        middle_index = len(x) // 2
    return middle_index


def median_index(x, i, j, k):
    """ Returns the median index of three when passed an array and indices of any 3 elements of that array """
    if (x[i] - x[j]) * (x[i] - x[k]) < 0:
        return i
    elif (x[j] - x[i]) * (x[j] - x[k]) < 0:
        return j
    else:
        return k


def quicksort_median_of_three(x):
    """ Counts number of comparisons while using Quick Sort with median-of-three element is chosen as pivot """
    # global count_pivot_median
    if len(x) == 1 or len(x) == 0:
        return x
    else:
        # count_pivot_median += len(x)-1
        k = median_index(x, 0, middle_index(x), -1)
        if k != 0: x[0], x[k] = x[k], x[0]
        i = 0
        for j in range(len(x) - 1):
            if x[j + 1] < x[0]:
                x[j + 1], x[i + 1] = x[i + 1], x[j + 1]
                i += 1
        x[0], x[i] = x[i], x[0]
        first_part = quicksort_median_of_three(x[:i])
        second_part = quicksort_median_of_three(x[i + 1:])
        first_part.append(x[i])
        return first_part + second_part
