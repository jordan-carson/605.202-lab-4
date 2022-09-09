from app.core.utils.utils import partition_quicksort as partition
from app.core.structures.stacks import Stack


def quicksort_iterative(array):
    left = 0
    right = len(array) - 1

    stack = Stack(len(array))
    stack.push(left)
    stack.push(right)

    while not stack.is_empty():
        right = stack.pop()
        left = stack.pop()

        pn = partition(array, left, right)

        if pn - 1 > left:
            stack.push(left)
            stack.push(pn - 1)

        if pn + 1 < right:
            stack.push(pn + 1)
            stack.push(right)


def quicksort_recursive(array, low, high):
    if low < high:

        p = partition(array, low, high)

        quicksort_recursive(array, low, p - 1) # left side
        quicksort_recursive(array, low + 1, high) # right side