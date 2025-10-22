"""
@file insertion_sort.py

@author Adam Pinkos
@date October 21, 2025
@course CS 4040 – Design and Analysis of Algorithms
@project Milestone 1 – Sorting Algorithm Runtime Analysis

@details
This file contains the implementation of the Insertion Sort algorithm.
Insertion Sort works by building a sorted portion of the array one element
at a time, inserting each new element into its correct position.

"""






def insertion_sort(arr):
    """"
    @brief In-place insertion sort.
    @param arr List of elements to sort.
    @return None
    
    """
    n = len(arr)

    # Already sorted array
    if n <= 1:
        return

    # Loop through the array starting from the 2nd element
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Shift elements that are greater than 'key' to one position ahead
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert key
        arr[j + 1] = key

