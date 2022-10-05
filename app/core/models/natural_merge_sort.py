from typing import List, TypeVar
from app.core.exceptions import NaturalMergeSortError

J = TypeVar("J")  # Always use J, instead of T :-D


def recursive_merge_sort(input_list):
    """
    Recursive Merge Sort

    Merge Sort is a DC (Divide and Conquer) algorithm.
    First, It divides the input array in two halves, calls itself for the two halves
    and then merges the two sorted halves. The merge function is used for merging two halves.

    Attributes:
    - Time Complexity: O(N*Log N)
    - Space Complexity: O(N)
    - Stable Sort, comparative to QuickSort for Lab 4.

    Args:
        input_list: list to be sorted

    Returns:
        sorted temporary list based on the input_list argument.
    """
    # if len(input_list) < 0:
    #     raise NaturalMergeSortError(f"{recursive_merge_sort.__name__} - Length of input array is empty, "
    #                                 f"size {len(input_list)}.")
    # Assigns the length of input list.
    size_of_input_list = len(input_list)

    # Creates a new list for sorted output list.
    temp_output_list = [None] * size_of_input_list

    # Sorts the input list.
    _sort_divided_sub_lists(input_list, temp_output_list, 0, size_of_input_list - 1)

    return temp_output_list


def _sort_divided_sub_lists(input_list, tmp_out_list, first_idx: int, last_idx: int):
    # Stop recursion if there is only one element in the sub-lists
    if first_idx == last_idx:
        return

    # Otherwise, calculates the middle point.
    mid_point = (first_idx + last_idx) // 2

    # Next, recursively call the two sub-lists
    _sort_divided_sub_lists(input_list, tmp_out_list, first_idx, mid_point)
    _sort_divided_sub_lists(input_list, tmp_out_list, mid_point + 1, last_idx)

    # Next, merges the two sub-lists.
    _merge_sub_lists(input_list, tmp_out_list, first_idx, mid_point, mid_point + 1, last_idx)

    # Copies the sorted part into the tmp_out_list.
    _copy_list(input_list, tmp_out_list, first_idx, last_idx)


def _copy_list(input_list, tmp_list, start: int, end: int):
    for i in range(start, end + 1):
        input_list[i] = tmp_list[i]


def _merge_sub_lists(input_list, tmp_out, first_start_index: int, first_end_index: int,
                     second_start_index: int, second_end_index: int):
    """
    This method merges two sorted sub-lists with three simple loops.

    Args:
        input_list:
        tmp_out:
        first_start_index:
        first_end_index:
        second_start_index:
        second_end_index:

    Returns:
        Merged sub_lists, this is done in-place as there is no return

    See Also:
        recursive_merge_sort

    """
    i = first_start_index
    j = second_start_index
    k = first_start_index

    while i <= first_end_index and j <= second_end_index:
        if input_list[i] <= input_list[j]:
            tmp_out[k] = input_list[i]
            i += 1
        else:
            tmp_out[k] = input_list[j]
            j += 1

        k += 1

    while i <= first_end_index:
        tmp_out[k] = input_list[i]
        i += 1
        k += 1

    while j <= second_end_index:
        tmp_out[k] = input_list[j]
        j += 1
        k += 1


# class NaturalMergeSort:
#     def __init__(self):
#         """
#         This will not be used as a class is not required.
#         """
#         pass
#
#     def recursive_merge_sort(self, input_list: List[J]) -> List[J]:
#         """
#         Recursive Merge Sort
#
#         Merge Sort is a DC (Divide and Conquer) algorithm.
#         First, It divides the input array in two halves, calls itself for the two halves
#         and then merges the two sorted halves. The merge function is used for merging two halves.
#
#         Attributes:
#         - Time Complexity: O(N*Log N)
#         - Space Complexity: O(N)
#         - Stable Sort, comparative to QuickSort for Lab 4.
#
#         Args:
#             input_list: list to be sorted
#
#         Returns:
#             sorted temporary list based on the input_list argument.
#         """
#
#         # Assigns the length of input list.
#         size_of_input_list = len(input_list)
#
#         # Creates a new list for sorted output list.
#         temp_output_list = [None] * size_of_input_list
#
#         # Sorts the input list.
#         self._sort_sub_lists_recursively(input_list, temp_output_list, 0, size_of_input_list - 1)
#
#         return temp_output_list
#
#     def _sort_sub_lists_recursively(self, input_list: List[J], tmp_out_list: List[J], first_idx: int, last_idx: int):  # -> List[T]
#         """
#         This method recursively sorts the divided sub-lists. This is a helper function to the main recursive_merge_sort
#         above.
#
#         Args:
#             input_list:
#             tmp_out_list:
#             first_idx:
#             last_idx:
#
#         Returns:
#
#         """
#         # Stop recursion if there is only one element in the sub-lists
#         if first_idx == last_idx:
#             return
#
#         # Otherwise, calculates the middle point.
#         mid_point = (first_idx + last_idx) // 2     # using floating point division to receive an integer
#
#         # Next, recursively call the two sub-lists
#         self._sort_sub_lists_recursively(input_list, tmp_out_list, first_idx, mid_point)
#         self._sort_sub_lists_recursively(input_list, tmp_out_list, mid_point + 1, last_idx)
#
#         # Next, merges the two sub-lists.
#         _merge_sub_lists(input_list, tmp_out_list, first_idx, mid_point, mid_point + 1, last_idx)
#
#         # Copies the sorted part into the tmp_out_list.
#         _copy_list(input_list, tmp_out_list, first_idx, last_idx)



