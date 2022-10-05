__doc__ = """
•	Select the first item of the partition as the pivot. Treat partitions of size one and two as stopping cases.
•	Same pivot selection. For a partition of size 100 or less, use an insertion sort to finish.  
•	Same pivot selection. For a partition of size 50 or less, use an insertion sort to finish.   
•	Select the median-of-three as the pivot. Treat partitions of size one and two as stopping cases.
"""

import random
from app.core.exceptions import QuicksortEmptyArrayException, QuicksortRecursionException, QuicksortStoppingCaseException
from app.core.models.insertion import insertion_sort

sort_kind = [0, 1, 2, 3] # we have 4 sorting methods to perform based on the pivot


def quicksort_recursive(array):
    """Sort the array by using quicksort."""
    if len(array) < 1:
        raise QuicksortEmptyArrayException

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]    # version 1
        for x in array:
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


def quicksort_stopping_cases(array, low, high, stopping_case: int):
    """
    This solves the first two stopping cases, when the pivot is less than 50, or 100
    Args:
        array:
        low:
        high:
        stopping_case:

    Returns:

    """
    if stopping_case not in [100, 50]:
        raise QuicksortStoppingCaseException("wrong stopping case")
    pivot: int = array[low]
    i = (high + 1)
    j = high

    while j > low:
        if high - low <= stopping_case:
            # use insertion sort to sort the array
            array = insertion_sort(array)
            break

        elif array[j] >= pivot:
            i -= 1
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
            # swap the items..

        j -= 1

    temp = array[i - 1]
    array[i - 1] = array[low]
    array[low] = temp
    return i - 1


def median_of_three(array, low, high):
    mid = (low + high - 1) // 2
    a, b, c = array[low], array[mid], array[high-1]
    if a <= b <= c:
        return b, mid
    if c <= b <= a:
        return b, mid
    if a <= c <= b:
        return c, high-1
    if b <= c <= a:
        return c, high-1
    return a, low






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