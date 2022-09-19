from typing import List, TypeVar
import random
from scipy import stats

T = TypeVar("T")


def recursive_merge_sort(input_list: List[T]) -> List[T]:
    """
    Recursive Merge Sort
    -----------------------------------------------
    Merge Sort is a Divide and Conquer algorithm.
    It divides the input array in two halves,
    calls itself for the two halves and then merges the two sorted halves.
    The merge function is used for merging two halves.

    Attributes:
    - Time Complexity: O(N*Log N)
    - Space Complexity: O(N)
    - Stable Sort
    """

    # Assigns the length of input list.
    size_of_input_list = len(input_list)

    # Creates a new list for sorted output list.
    temp_output_list = [None] * size_of_input_list

    # Sorts the input list.
    recursive_sort(input_list, temp_output_list, 0, size_of_input_list - 1)

    return temp_output_list


def recursive_sort(input_list: List[T], temp_output_list: List[T], first_index: int, last_index: int) : #-> List[T]
    """
    This method recursively sorts the divided sublists
    """

    # Stops the recursion if there is only one element in the sublists.
    if first_index == last_index:
        return

    # Otherwise, calculates the middle point.
    mid_index = (first_index + last_index) // 2

    # Then, calls the two sublists recursively.
    recursive_sort(input_list, temp_output_list, first_index, mid_index)
    recursive_sort(input_list, temp_output_list, mid_index + 1, last_index)

    # Merges the two sublists.
    merge_sublists(input_list, temp_output_list, first_index,
                   mid_index, mid_index + 1, last_index)

    # Copies the sorted part into the temp_output_list.
    copy_list(input_list, temp_output_list, first_index, last_index)


def merge_sublists(input_list: List[T], temp_output_list: List[T],
                   first_start_index: int, first_end_index: int,
                   second_start_index: int, second_end_index: int) -> List[T]:
    """
        This method merges the two sorted sublists with three simple loops:
        - If both sublists 1 and 2 have elements to be placed in the output merged list
        - If sublists 1 has some elements left to be placed in the output merged list
        - If sublists 2 has some elements left to be placed in the output merged list

        e.g., sublist 1 [1, 3, 5, 7, 9]
        e.g., sublist 2 [2, 4, 6, 8, 10, 12, 14]

        - First while loop generates: [1, 2, 3, 4, 5, 6 , 7, 8, 9, 10]
        - Second while loop just passes, since no elements left from the first sublist.
        - Third while loop generates: [1, 2, 3, 4, 5, 6 , 7, 8, 9, 10, 12, 14]

    """
    i = first_start_index
    j = second_start_index
    k = first_start_index

    while i <= first_end_index and j <= second_end_index:
        if input_list[i] <= input_list[j]:
            temp_output_list[k] = input_list[i]
            i += 1
        else:
            temp_output_list[k] = input_list[j]
            j += 1

        k += 1

    while i <= first_end_index:
        temp_output_list[k] = input_list[i]
        i += 1
        k += 1

    while j <= second_end_index:
        temp_output_list[k] = input_list[j]
        j += 1
        k += 1


def copy_list(input_list: List[T], temp_output_list: List[T], first_index: int, end_index: int) -> List[T]:
    for i in range(first_index, end_index+1):
        input_list[i] = temp_output_list[i]