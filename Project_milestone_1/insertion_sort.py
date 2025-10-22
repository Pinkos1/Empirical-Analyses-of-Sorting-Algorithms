
""""

CS 4040 – Design and Analysis of Algorithms
Project 1 – Sorting Algorithm Runtime Analysis
Author: Adam Pinkos
Date: October 21st, 2025
File: insertion_sort.py

Description:

"""


"""Insertion Sort Implementation"""
def insertion_sort(arr):
    # Number of elements in array
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

