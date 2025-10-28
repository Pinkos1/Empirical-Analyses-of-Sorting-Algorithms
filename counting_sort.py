"""
@file counting_sort.py

@author Adam Pinkos
@date October 27th, 2025
@course CS 4040 – Design and Analysis of Algorithms
@project Milestone 2 – Sorting Algorithm Runtime Analysis

@details

"""

import random
import time



def counting_sort(arr, k):
    """
    @brief Sorts an array of non-negative integers using Counting Sort.
    @param arr The list of integers to be sorted
    @param k The maximum integer value in the array.
    @return A new sorted list containing the same elements as arr.
    """

    n = len(arr)
    x = [0] * n        
    y = [0] * (k + 1)  

    # Loop 1
    for i in range(k + 1):
        y[i] = 0

    # Loop 2
    for j in range(n):
        y[arr[j]] = y[arr[j]] + 1

    # Loop 3
    for i in range(1, k + 1):
        y[i] = y[i] + y[i - 1]

    # Loop 4 stable
    for j in range(n - 1, -1, -1):
        x[y[arr[j]] - 1] = arr[j]
        y[arr[j]] = y[arr[j]] - 1

    return x





