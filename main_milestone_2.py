
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
        print("\nTesting CountingSort with n =", size)


        # Two different values for k 
        k_squared = size * size
        if k_squared <= 1_000_000:   # max K 
            k_values = [10, k_squared]
        else:
            k_values = [10, size]
    

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

             # Save results for the final table: (n, k, Algorithm(params), median_ms)
            cs_medians.append((size, k, f"CountingSort(k={k})", round(median_time, 3)))


    print("\n=== Runtime Table (Median of 5 runs) ===")
    print("{:>8}  {:>12}  {:<24}  {:>12}".format("n", "k (max)", "Algorithm (params)", "Median (ms)"))
    for row in cs_medians:
        n_val, k_val, algo, med = row
        print("{:>8}  {:>12}  {:<24}  {:>12.3f}".format(n_val, k_val, algo, med))




    # Graph to plot median runtimes 

    # Create two lists for each k group
    k10 = []
    med_k10 = []
    k_square = []
    med_k_square = []

    # Cycle through all results and separate them by k value
    for row in cs_medians:
        n_val = row[0]
        k_val = row[1]
        median_val = row[3]

        if k_val == 10:
            k10.append(n_val)
            med_k10.append(median_val)
        else:
            k_square.append(n_val)
            med_k_square.append(median_val)

    # Make the graph
    plt.figure(figsize = (6, 5))
    plt.plot(k10, med_k10, marker = 'o', label = 'CountingSort (k=10)')
    plt.plot(k_square, med_k_square, marker = 'o', label = 'CountingSort (k=n² or n)')

    # Labels and title
    plt.xlabel('Input Size (n)')
    plt.ylabel('Median Runtime (ms)')
    plt.title('Counting Sort Runtime (Milestone 2)')
    plt.legend()
    plt.grid(True)


    plt.show()





if __name__ == "__main__":
    main()