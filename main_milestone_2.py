
"""
@file main_milestone_2.py

@author Adam Pinkos
@date October 27th, 2025
@course CS 4040 – Design and Analysis of Algorithms
@project Milestone 2 – Sorting Algorithm Runtime Analysis

@details

"""

import random
import time
import matplotlib.pyplot as plt
from counting_sort import counting_sort




def median_of_five(values):
    """
    @brief Calculates the median of a list of five runtime values.
    @param values A list containing five numeric runtime measurements.
    @return The median value from the list.
    """
    s = sorted(values)
    return s[2]



def main():

    cs_medians = []

    # Input sizes 
    n = [10, 100, 1000, 2000, 5000, 10000, 20000]

    # Loop through each input size
    for size in n:

        # Two different values for k 
        k_values = [10, size]
        k_squared = size * size
        if k_squared <= 1000000:  # max K
            k_values.append(k_squared)
    

        # Run the experiments for each k value
        for k in k_values:
            print("  k =", k)
            cs_trials = []

            # Run 5 trials
            for trial in range(5):

                # Make a random array with numbers between 0 and k
                arr = []
                for i in range(size):
                    arr.append(random.randint(0, k))

                # Start timer
                start = time.perf_counter()

                # Run Counting Sort
                counting_sort(arr, k)

                # End timer
                end = time.perf_counter()

                # Calculate runtime in milliseconds
                runtime_ms = (end - start) * 1000
                cs_trials.append(runtime_ms)

            # Compute median of 5 trials
            median_time = median_of_five(cs_trials)

            # Print the median runtime for this (n, k)
            print("    Median runtime:", round(median_time, 3), "ms")

            # Save results if needed later for plotting
            cs_medians.append((size, k, median_time))





if __name__ == "__main__":
    main()