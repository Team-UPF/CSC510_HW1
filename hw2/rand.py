"""
This module provides utilities for generating random arrays.
"""
import random

def random_array(arr):
    """
    Fills an array with random numbers using Python's random module.

    Args:
        arr (list): An empty list that will be filled with random numbers.

    Returns:
        list: The array filled with random integers.
    """
    for i, _ in enumerate(arr):
        arr[i] = random.randint(1, 20)  # Generates a random integer between 1 and 20
    return arr
