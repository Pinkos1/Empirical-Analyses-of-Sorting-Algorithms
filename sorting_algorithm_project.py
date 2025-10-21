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
            arr[j + 1] = arr[j]
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



def median_of_five(values):
    # sort the 5 runtimes and take the middle one
    s = sorted(values)
    return s[2]


def main():

    # Different input sizes for testing runtime
    n = [10, 100, 1000, 2000, 5000, 10000, 20000]

    # Loop through all sizes
    for i in n:

        # Insertion Sort
        ins_trials = []  

        for trial in range(5):  # run 5 trials
            # make a random list with n numbers between 0 and 10000
            arr = []
            for k in range(i):
                arr.append(random.randint(0, 10000))

            # start timer
            start = time.perf_counter()

            # run the sorting algorithm
            insertion_sort(arr)

            # stop timer
            end = time.perf_counter()

            # calculate runtime in milliseconds
            runtime_ms = (end - start) * 1000
            ins_trials.append(runtime_ms)

        # find median of 5 runtimes
        ins_median = median_of_five(ins_trials)
        print("n =", n, "Insertion Sort median runtime (ms):", round(ins_median, 2))




        # Randomized Quicksort
        qs_trials = []  

        for trial in range(5):  # run 5 trials
            # make a random list with n numbers between 0 and 10000
            arr = []
            for k in range(i):
                arr.append(random.randint(0, 10000))

            # start timer
            start = time.perf_counter()

            # run the sorting algorithm
            randomized_quicksort(arr, 0, len(arr) - 1)

            # stop timer
            end = time.perf_counter()

            # calculate runtime in milliseconds
            runtime_ms = (end - start) * 1000
            qs_trials.append(runtime_ms)

        # find median of 5 runtimes
        qs_median = median_of_five(qs_trials)
        print("n =", n, "Randomized Quicksort median runtime (ms):", round(qs_median, 2))


if __name__ == "__main__":
    main()
