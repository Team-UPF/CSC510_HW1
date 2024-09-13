"""
This module provides a merge sort implementation and helper functions
to sort an array using the divide and conquer method.
"""


import rand


def merge_sort(input_arr):
    """
    Sorts an array using the merge sort algorithm.

    Args:
        input_arr (list): The array to be sorted.

    Returns:
        list: The sorted array.
    """
    if len(input_arr) <= 1:
        return input_arr
    half =len(input_arr) // 2

    # Split and recursively merge sort
    left_half = merge_sort(input_arr[:half])
    right_half = merge_sort(input_arr[half:])

    # Combine sorted halves
    return recombine(left_half, right_half)
def recombine(left_arr, right_arr):
    """
    Merges two sorted lists into a single sorted list.

    Args:
        left_arr (list): The left sublist.
        right_arr (list): The right sublist.

    Returns:
        list: A merged and sorted list.
    """
    merged = []
    left_index = right_index = 0

    # Merge the two sorted halves
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merged.append(left_arr[left_index])
            left_index += 1
        else:
            merged.append(right_arr[right_index])
            right_index += 1

    # Add remaining elements from both halves
    merged.extend(left_arr[left_index:])
    merged.extend(right_arr[right_index:])

    return merged


# Example array to test
arr = rand.random_array([None] * 20)
arr_out = merge_sort(arr)
print(arr_out)
