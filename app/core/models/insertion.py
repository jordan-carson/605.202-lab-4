def insertion_sort(array):
    for i in range(1, len(array)):
        k = array[i]
        j = i - 1
        while j >= 0 and array[j] > k:

            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = k

    return array
