"""
@file randomized_quicksort.py
@brief Implements the Randomized Quicksort algorithm used for runtime analysis.

@author Adam Pinkos
@date October 21, 2025
@course CS 4040 – Design and Analysis of Algorithms
@project Milestone 1 – Sorting Algorithm Runtime Analysis

@details
This file contains the implementation of the Randomized Quicksort algorithm.
It includes three main functions: partition(), randomize_partition(), and
randomized_quicksort(). The algorithm works by choosing a random pivot element,
partitioning the array around that pivot, and then recursively sorting the
left and right subarrays. Randomization helps avoid worst-case performance on
already sorted or patterned datasets, achieving an average-case runtime of
O(n log n).
"""

import random

""" Randomize Quicksort Implementation"""

def partition(arr, left, right):
    """
    @brief partition using arr[right] as pivot.
    @param arr List to partition.
    @param left Left index.
    @param right Right index.
    @return int Final pivot index.

    """
    pivot = arr[right]
    i = left - 1

    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


def randomize_partition(arr, left, right):
    """
    @brief Picks a random pivot index, swaps to end, then partitions.
    @param arr List to partition.
    @param left Left index.
    @param right Right index.
    @return int Final pivot index.

    """
    pivot_index = random.randint(left, right)
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]  

    return partition(arr, left, right)

def randomized_quicksort(arr, left, right):
    """
    @brief Recursive randomized quicksort.
    @param arr List to sort.
    @param left Starting index of subarray.
    @param right Ending index of subarray.
    @return None

    """
    if left < right:
        pivot_index = randomize_partition(arr, left, right)
        
        randomized_quicksort(arr, left, pivot_index - 1)
        randomized_quicksort(arr, pivot_index + 1, right)