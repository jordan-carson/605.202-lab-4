from app.core.utils.utils import swap


def heapsort(array):

    for i in range((len(array) // 2) - 1, 0, -1):
        heapify(array, len(array), i)

    for i in range(len(array) - 1, 0, -1):
        tmp = array[0]
        array[0], array[i] = array[i], tmp

        heapify(array, i, 0)


def heapify(array, n, i):

    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and array[left] > array[largest]:
        largest = left

    if right < n and array[right] > array[largest]:
        largest = right

    if largest != i:
        array[largest], array[i] = array[i], array[largest]

    heapify(array, n, largest)

