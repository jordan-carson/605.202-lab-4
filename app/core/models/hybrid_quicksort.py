def insertion_sort(arr, low, high):
    for i in range(low + 1, high + 1):
        val = arr[i]
        j = i

        while j > low and arr[j - 1] > val:
            arr[j] = arr[j - 1]
            j -= 1

        arr[j] = val

    return


def partition(arr, low, high):
    pivot = arr[high]
    j = low
    for i in range(low, high):
        if arr[i] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    arr[j], arr[high] = arr[high], arr[j]
    return j


def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot+1, high)
        return arr


def hybrid_quicksort_100(arr, low, high):
    while low < high:

        if high - low + 1 < 100:
            insertion_sort(arr, low, high) # used for stopping cases of 50, 100
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
            insertion_sort(arr, low, high) # used for stopping cases of 50, 100
            break

        else:
            pivot = partition(arr, low, high)

            if pivot - low < high - pivot:
                hybrid_quicksort_50(arr, low, pivot - 1)
                low = pivot + 1

            else:
                hybrid_quicksort_50(arr, pivot + 1, high)
                high = pivot - 1


