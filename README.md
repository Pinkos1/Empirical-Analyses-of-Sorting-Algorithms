# Empirical Analyses of Sorting Algorithms


**Author:** Adam Pinkos   
**Course:** CS 4040 – Design and Analysis of Algorithms  
**Instructor:** Dr. Majid Mirzanezhad  
**Date:** October 21st, 2025 

# Overview
This project is part of **CS 4040 – Design and Analysis of Algorithms**.  
It explores the **empirical runtime behavior** of sorting algorithms by implementing, timing, and later visualizing their performance.git pull --rebase origin main

- Insertion Sort
- Randomized Quicksort



## Algorithms Implemented ##

# Insertion Sort
Insertion Sort builds the sorted portion of an array one element at a time.  
It’s simple and efficient for small or nearly sorted datasets.

# Randomized Quicksort
Randomized Quicksort uses a random pivot to divide the array into subarrays, reducing the chance of encountering the worst-case scenario.


## Build / Run Instructions ##

Python 3.10 or newer
matplotlib library


pip install matplotlib

python main_runtime.py



Running those will:

1. Warm up both algorithms.

2. Test input sizes: 10, 100, 1000, 2000, 5000, 10000, 20000.

3. Perform 5 trials per n, computing the median runtime for each algorithm.

4. Print the median times to the terminal.

5. Generate and display a runtime comparison plot.



| Algorithm                | File Name                 | Description                                                                                                                     |
| ------------------------ | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| **Insertion Sort**       | `insertion_sort.py`       | A simple O(n²) algorithm that builds a sorted list one item at a time. Best for small or nearly sorted datasets.                |
| **Randomized Quicksort** | `randomized_quicksort.py` | A divide-and-conquer algorithm that randomly selects a pivot to minimize the chance of worst-case behavior. Average O(n log n). |



When you run the program, the console shows something like:


n = 100 Insertion Sort median runtime (ms): 0.53

n = 100 Randomized Quicksort median runtime (ms): 0.09

n = 1000 Insertion Sort median runtime (ms): 27.41

n = 1000 Randomized Quicksort median runtime (ms): 2.13
...




