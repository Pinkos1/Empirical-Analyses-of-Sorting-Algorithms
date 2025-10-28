# CS 4040 – Milestone 2  
# Counting Sort Runtime Analysis

**Author:** Adam Pinkos  
**Date:** October 27th, 2025  
**Course:** CS 4040 – Design and Analysis of Algorithms  
**Project:** Milestone 2  

### How to run 
python main_milestone_2.py


###  Overview
This project measures and analyzes the runtime performance of **Counting Sort** using different input sizes and parameter values of `k`.  
The experiment follows the Milestone 2 guidelines, running the algorithm multiple times for various `(n, k)` combinations and recording the **median runtime** in milliseconds.

###  Algorithm
Counting Sort is a non-comparison-based sorting algorithm with a time complexity of **O(n + k)**, where  
- `n` = number of elements, and  
- `k` = the maximum integer value in the input.  

It is efficient when `k` is not drastically larger than `n`.

### Experimental Setup
- **Input sizes (n):** 10, 100, 1000, 2000, 5000, 10000, 20000  
- **k values:** 10 and n² (if n² ≤ 1,000,000; otherwise n)  
- **Trials per (n, k):** 5  
- **Statistic reported:** Median runtime (ms)  
- **Timer used:** `time.perf_counter()`  
- **Graphing library:** Matplotlib  


###  Results Summary
- For **small k (= 10)**, runtime increases **almost linearly** with n, following O(n + k) ≈ O(n).  
- For **large k (= n² or n)**, runtimes grow sharply because the algorithm must allocate and loop through a much larger counting array.  
- The experimental data matches theoretical expectations.

---

###  Output Example
The program prints a console table:
<img width="520" height="294" alt="image" src="https://github.com/user-attachments/assets/be08a284-2e6d-416b-956e-d95958da4557" />





