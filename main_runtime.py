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
from Project_milestone_1.insertion_sort import insertion_sort
from Project_milestone_1.randomized_quicksort import randomized_quicksort

def median_of_five(values):
    # Sort the 5 runtimes and take the middle one
    s = sorted(values)
    return s[2]

def main():

    # Store the median trials
    ins_medians = []
    qs_medians = []

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
        print("n =", i, "Insertion Sort median runtime (ms):", round(ins_median, 2))
        ins_medians.append(ins_median)

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
        print("n =", i, "Randomized Quicksort median runtime (ms):", round(qs_median, 2))
        qs_medians.append(qs_median)



    # Graph to plot median runtimes 
    fig, ax = plt.subplots(figsize = (6, 5))      

    # Plot both algorithms
    ax.plot(n, ins_medians, marker = 'o', color = 'Blue', linewidth = 2, label='Insertion Sort')
    ax.plot(n, qs_medians, marker = 'o', color = 'Orange', linewidth = 2, label = 'Randomized Quicksort')

    # Labels and title
    ax.set_xlabel('Input Size (n)', fontsize = 11, fontweight = 'bold')
    ax.set_ylabel('Median Runtime (ms)', fontsize = 11, fontweight = 'bold')
    ax.set_title('Runtime Comparison: Insertion Sort vs. Randomized Quicksort',
                 fontsize = 13, fontweight = 'bold', pad = 15)

    # Grid, legend, and layout tweaks
    ax.grid(True, linestyle = '--', linewidth = 0.6, alpha = 0.7)
    ax.legend(facecolor = 'white', framealpha = 1, edgecolor = 'black')
    plt.tight_layout()

    plt.show()





""" Test functions for sorting algorithms """

def TestMe_InsertionSort():
    # makes random list 
    arr = []
    for i in range(20):
        arr.append(random.randint(0,100))

    sorted_arr = sorted(arr)
    insertion_sort(arr)

    if arr == sorted_arr:
        print("Insertion Sort Tests Passed")
    else:
        print("Insertion Sort failed")


def TestMe_RandomizedQuicksort():
    
    arr = []
    for i in range(20):
        arr.append(random.randint(0,100))

    sorted_arr = sorted(arr)
    randomized_quicksort(arr, 0, len(arr)-1)

    if arr == sorted_arr:
        print("Randomized Quicksort Tests Pass")
    else:
        print("Randomized Quicksort failed")


if __name__ == "__main__":
    main()
    TestMe_InsertionSort()
    TestMe_RandomizedQuicksort()