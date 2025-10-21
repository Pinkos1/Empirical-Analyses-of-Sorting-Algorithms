"""
CS 4040 – Design and Analysis of Algorithms
Project 1 – Sorting Algorithm Runtime Analysis
Author: Adam Pinkos
Date: October 21st, 2025

Description:

"""


import random
import time
import matplotlib.pyplot as plt




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
            arr[j + 1] = arr[j]   #
            j -= 1

        # Insert key
        arr[j + 1] = key



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

        



    