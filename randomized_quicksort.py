
""""
CS 4040 – Design and Analysis of Algorithms
Project 1 – Sorting Algorithm Runtime Analysis
Author: Adam Pinkos
Date: October 21st, 2025
File: randomized_quicksort.py

Description:

"""

import random

""" Randomize Quicksort Implementation"""

def partition(arr, left, right):

    pivot = arr[right]
    i = left - 1

    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


def randomize_partition(arr, left, right):
    pivot_index = random.randint(left, right)
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]  

    return partition(arr, left, right)

def randomized_quicksort(arr, left, right):
    if left < right:
        pivot_index = randomize_partition(arr, left, right)
        
        randomized_quicksort(arr, left, pivot_index - 1)
        randomized_quicksort(arr, pivot_index + 1, right)