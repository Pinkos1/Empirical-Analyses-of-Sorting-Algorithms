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
from insertion_sort import insertion_sort
from randomized_quicksort import randomized_quicksort



def median_of_five(values):
    # Sort the 5 runtimes and take the middle one
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
