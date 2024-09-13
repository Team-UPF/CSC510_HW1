"""
Test cases for the merge_sort function.
"""
from hw2_debugging import merge_sort


def test_empty_array():
    """
    Test merge_sort with an empty array.
    Ensures that sorting an empty array returns an empty array.
    """
    assert merge_sort([]) == []

def test_sorted_array():
    """
    Test merge_sort with an already sorted array.
    Ensures that sorting a sorted array returns the same array.
    """
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_unsorted_array():
    """
    Test merge_sort with an unsorted array.
    Ensures that sorting an unsorted array returns a correctly sorted array.
    """
    assert merge_sort([5, 3, 1, 4, 2])== [1, 2, 3, 4, 5]
