def insertion_sort(arr, low, n):
    for i in range(low + 1, n + 1):
        val = arr[i]
        j = i

        while j > low and arr[j - 1] > val:
            arr[j] = arr[j - 1]
            j -= 1

        arr[j] = val

    return


