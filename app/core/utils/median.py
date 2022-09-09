from core.utilities.utils import swap


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


def partition(array, left, right):
    median(array, left, right)

    pivot = array[right]

    i = left - 1

    for j in range(right - 1):
        if array[j] <= pivot:
            i += 1
            swap(array, i, j)

    swap(array, i+1, right)
    return i+1