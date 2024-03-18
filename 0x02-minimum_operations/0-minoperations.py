#!/usr/bin/python3
"""
dynamic programming
"""


def minOperations(n):
    """
    function to calculate min number of operations needed to
    result in exactly n H characters in the file
    """
    if n <= 0:
        return 0

    # Initialize variables
    operations = 0  # Total number of operations
    buffer_size = 1  # Current number of 'H' characters in the buffer
    clipboard = 0  # Number of 'H' characters in the clipboard

    while buffer_size < n:
        if n % buffer_size == 0:
            clipboard = buffer_size
            operations += 1

        operations += 1  # Paste operation
        buffer_size += clipboard

    return operations
