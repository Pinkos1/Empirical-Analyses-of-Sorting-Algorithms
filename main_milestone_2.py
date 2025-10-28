

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

    # Different input sizes for testing runtime
    n = [10, 100, 1000, 2000, 5000, 10000, 20000]


    for i in n:
        k_value = [10, i]
        k_squared = i * i


        for k in k_value:
            cs_trials = []

            for trial in range(5):
                arr = []
                for i in range(n):
                    arr.append(random.randint(0, k))
                
                start = time.perf_counter()

                counting_sort(arr, k)

                end = time.perf_counter()

                runtime_ms = (end - start) * 1000
                cs_trials.append(runtime_ms)

                median_time = median_of_five(cs_trials)
        
    