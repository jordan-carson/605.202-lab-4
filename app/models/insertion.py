
def insertion_sort_hybrid(arr, low, high):
    """

    Args:
        arr: array like data structure
        low: integer for the low end, mostly set to 0
        high: integer for the high end, mostly set to len(array) - 1

    Returns:
        performs insertion-sort in-place
    """
    for i in range(low + 1, high + 1):
        val = arr[i]
        j = i

        while j > low and arr[j - 1] > val:
            arr[j] = arr[j - 1]
            j -= 1

        arr[j] = val
