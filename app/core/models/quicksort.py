__doc__ = """
•	Select the first item of the partition as the pivot. Treat partitions of size one and two as stopping cases.
•	Same pivot selection. For a partition of size 100 or less, use an insertion sort to finish.  
•	Same pivot selection. For a partition of size 50 or less, use an insertion sort to finish.   
•	Select the median-of-three as the pivot. Treat partitions of size one and two as stopping cases.
"""

import random
from app.core.exceptions import QuicksortEmptyArrayException, QuicksortRecursionException


def quicksort_recursive(array):
    """Sort the array by using quicksort."""

    # if len(array) < 1:
    #     raise QuicksortEmptyArrayException

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]    # version 1
        for x in array:
            # equal.append(x) if x == pivot else
            # if x == pivot:
            #     equal.append(x)
            # elif x < pivot:
            #     less.append(x)
            # else:
            #     greater.append(x)
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quicksort_recursive(less) + equal + quicksort_recursive(greater)
    else:
        return array
    # return array


def quicksort_recursive2(array):
    """
     random pivot location quicksort. uses extra memory.
    :param array:
    :return:
    """
    smaller = []
    bigger = []
    if len(array) <= 1:
        return array
    _pivot = array[random.randint(0, len(array)-1)]
    array.remove(_pivot)
    for items in array:
        if items <= _pivot:
            smaller.append(items)
        else:
            bigger.append(items)
    return concat(quicksort_recursive2(smaller), _pivot, quicksort_recursive2(bigger))


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
    # res.append(pivot)


# def quicksort_iterative(array):
#     left = 0
#     right = len(array) - 1
#
#     stack = Stack(len(array))
#     stack.push(left)
#     stack.push(right)
#
#     while not stack.is_empty():
#         right = stack.pop()
#         left = stack.pop()
#
#         pn = partition(array, left, right)
#
#         if pn - 1 > left:
#             stack.push(left)
#             stack.push(pn - 1)
#
#         if pn + 1 < right:
#             stack.push(pn + 1)
#             stack.push(right)
#     return stack.pop()
#
#
# def quicksort_recursive(array, low, high):
#     if low < high:
#         p = partition(array, low, high)
#         quicksort_recursive(array, low, p - 1) # left side
#         quicksort_recursive(array, low + 1, high) # right side