

"""
This module provides utilities for generating random arrays.
"""

import subprocess


def random_array(arr):
    """
    Fills an array with random numbers using the 'shuf' command.

    Args:
        arr (list): An empty list that will be filled with random numbers.

    Returns:
        list: The array filled with random integers.
    """
    for i, _ in enumerate(arr):
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"],
            capture_output=True,
            check=True
        )
        arr[i] = int(shuffled_num.stdout)
    return arr
