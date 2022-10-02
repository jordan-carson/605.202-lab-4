def insertion_sort(array):
    for i in range(1, len(array)):
        k = array[i]
        j = i - 1
        while j >= 0 and array[j] > k:

            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = k

    return array


def insertion2(arr):

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

