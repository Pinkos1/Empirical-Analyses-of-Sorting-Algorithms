
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


    n_k10 = []
    med_k10 = []

    n_kn = []
    med_kn = []

    n_k2 = []
    med_k2 = []

    # Loop through each input size
    for size in n:
        print("\nTesting CountingSort with n =", size)


         
        # Three different values for k: 10, n, n²
        k_10 = 10
        k_n = size
        k_n_squared = size * size

        # Cap k if it exceeds the limit
        if k_n_squared > 1_000_000:
            print(f"  (Capped k squared at 1,000,000 for n = {size})")
            k_n_squared = 1_000_000

        k_values = [k_10, k_n, k_n_squared]


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


            if k == 10:
                n_k10.append(size)
                med_k10.append(round(median_time, 3))
            elif k == size:
                n_kn.append(size)
                med_kn.append(round(median_time, 3))
            else:
                # treat as n^2 (possibly capped)
                n_k2.append(size)
                med_k2.append(round(median_time, 3))


    # Table in the console 
    print("\n=== Runtime Table (Median of 5 runs) ===")
    print("{:>8}  {:>12}  {:<24}  {:>12}".format("n", "k (max)", "Algorithm (params)", "Median (ms)"))
    for row in cs_medians:
        n_val, k_val, algo, med = row
        print("{:>8}  {:>12}  {:<24}  {:>12.3f}".format(n_val, k_val, algo, med))



    # Graph 1 k = 10 
    plt.figure(figsize = (6, 5))
    plt.plot(n_k10, med_k10, marker = 'o', label = 'CountingSort (k = 10)')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Median Runtime (ms)')
    plt.title('k = 10')
    plt.legend()
    plt.grid(True)

    # Note on the plot
    plt.text(0.5, -0.22,
             "For k = 10, runtime grows almost linearly with n (O(n + k) = O(n)).",
             fontsize = 9, ha = 'center', va = 'center', transform = plt.gca().transAxes)
    plt.tight_layout()
    plt.show()



    # Graph 2 k = n 
    plt.figure(figsize = (6, 5))
    plt.plot(n_kn, med_kn, marker = 'o', label = 'CountingSort (k = n)')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Median Runtime (ms)')
    plt.title('k = n')
    plt.legend()
    plt.grid(True)

    # Note on the plot
    plt.text(0.5, -0.22,
             "For k=n, runtime increases faster than for k=10\n"
             "because the counting array grows with n.",
             fontsize = 9, ha = 'center', va = 'center', transform = plt.gca().transAxes)
    plt.tight_layout()
    plt.show()




    # Graph 3 k = n squared
    plt.plot(n_k2, med_k2, marker = 'o', label = 'CountingSort (k = n squared)')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Median Runtime (ms)')
    plt.title('k = n squared')
    plt.legend()
    plt.grid(True)

    # Note on the plot
    plt.text(0.5, -0.28,
             "For k=n squared, runtime is dominated by k due to the large counting array.\n"
             "Note: For large n, k squared values above 1,000,000 were capped to avoid memory issues.",
             fontsize = 9, ha = 'center', va = 'center', transform = plt.gca().transAxes)
    plt.tight_layout()
    plt.show()


  
def TestMe_counting_sort():
    """
    @brief Test function for verifying Counting Sort.
    @details
    Generates a small random list and compares the output of
    counting_sort() with Python's built-in sorted() function.
    This ensures that Counting Sort produces the correct order.
    """
    arr = []

    # Max value in array
    k = 50 
    for i in range(20):
        arr.append(random.randint(0, k))

    # Expected sorted array 
    expected = sorted(arr)

    result = counting_sort(arr, k)

    # Verify output matches the expected result
    assert result == expected, "Counting Sort failed"
    print("Counting Sort Tests Passed")


if __name__ == "__main__":
    main()
    TestMe_counting_sort
