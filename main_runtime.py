"""
@file main_runtime.py
@brief Runs empirical runtime tests for Insertion Sort and Randomized Quicksort.

@author Adam Pinkos
@date October 21, 2025
@course CS 4040 – Design and Analysis of Algorithms
@project Milestone 1 – Sorting Algorithm Runtime Analysis

@details
This file acts as the main driver program for analyzing the performance of
Insertion Sort and Randomized Quicksort. 
"""



import random
import time
import matplotlib.pyplot as plt
from insertion_sort import insertion_sort
from randomized_quicksort import randomized_quicksort

def median_of_five(values):
    """
    @brief Calculates the median of a list of five runtime values.
    @param values A list containing five numeric runtime measurements.
    @return The median value from the list.

    """
    s = sorted(values)
    return s[2]

def main():
    """
    @brief Main function for runtime testing.
    @details
    This function executes multiple trials of both sorting algorithms,
    records their runtimes, prints the median runtimes, and generates
    a comparison plot.

    """
    # Warm up before timing 
    nums = []
    for i in range(500):
        nums.append(random.randint(0, 10000))
        insertion_sort(nums)

    nums = []
    for i in range(500):
        nums.append(random.randint(0, 10000))
        randomized_quicksort(nums, 0, len(nums) - 1)

    # Store the median trials
    ins_medians = []
    qs_medians = []

    # Different input sizes for testing runtime
    n = [10, 100, 1000, 2000, 5000, 10000, 20000]

    # Loop through all sizes
    for i in n:

        # Insertion Sort
        ins_trials = []

        for trial in range(5): 
            # Make a random list with n numbers between 0 and 10000
            arr = []
            for k in range(i):
                arr.append(random.randint(0, 10000))

            # Start timer
            start = time.perf_counter()

            # Run the sorting algorithm
            insertion_sort(arr)

            # Stop timer
            end = time.perf_counter()

            # Calculate runtime in milliseconds
            runtime_ms = (end - start) * 1000
            ins_trials.append(runtime_ms)

        # Find median of 5 runtimes
        ins_median = median_of_five(ins_trials)
        print("n =", i, "Insertion Sort median runtime (ms):", round(ins_median, 2))
        ins_medians.append(ins_median)

        # Randomized Quicksort
        qs_trials = []

        for trial in range(5):  
            # Make a random list with n numbers between 0 and 10000
            arr = []
            for k in range(i):
                arr.append(random.randint(0, 10000))

            # Start timer
            start = time.perf_counter()

            # Run the sorting algorithm
            randomized_quicksort(arr, 0, len(arr) - 1)

            # Stop timer
            end = time.perf_counter()

            # Calculate runtime in milliseconds
            runtime_ms = (end - start) * 1000
            qs_trials.append(runtime_ms)

        # Find median of 5 runtimes
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






def TestMe_InsertionSort():
    """
    @brief Test function for verifying Insertion Sort.
    @details
    Generates a small random list and compares the output of
    insertion_sort() with Python's built-in sorted() function.

    """
    arr = []
    for i in range(20):
        arr.append(random.randint(0,100))
    sorted_arr = sorted(arr)
    
    insertion_sort(arr)
    assert arr == sorted_arr, "Insertion Sort failed"   
    print("Insertion Sort Tests Passed")


def TestMe_RandomizedQuicksort():
    """
    @brief Test function for verifying Randomized Quicksort.
    @details
    Generates a small random list and compares the output of
    randomized_quicksort() with Python's built-in sorted() function.

    """
    arr = []
    for i in range(20):
        arr.append(random.randint(0,100))

    sorted_arr = sorted(arr)
    randomized_quicksort(arr, 0, len(arr)-1)
    assert arr == sorted_arr, "Randomized Quicksort failed"  # required assert
    print("Randomized Quicksort Tests Pass")


if __name__ == "__main__":
    main()
    TestMe_InsertionSort()
    TestMe_RandomizedQuicksort()