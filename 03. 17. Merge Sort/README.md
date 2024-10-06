# Merge Sort 🗂️

![Merge-sort-example-300px](https://github.com/user-attachments/assets/5035157a-e8a5-456a-8a73-e02b8fa315e6)

*gif source: Wikimedia Commons*

- It is more predictable in terms of performance and is stable,.
- It’s particularly useful when stability is a requirement or when working with linked lists.
- Algorithm Type: Comparison-based, divide-and-conquer.
  
## Approach:
  - Dividing: Merge Sort divides the array into two halves until each sub-array contains a single element.
  - Merging: It then merges these sub-arrays to produce sorted arrays.

## Time Complexity:

  - All Cases: O(n log n) (Merge Sort has consistent performance regardless of the input data)

- Space Complexity: O(n) due to the need for temporary arrays used during merging.
- Stability: Stable. Equal elements retain their relative order.
- Not In-Place: Merge Sort requires additional space proportional to the size of the array.

### Applications:
  - Data Analysis: Applied in sorting large-scale data for statistical analysis and data processing tasks.
  - Computational Geometry: Used in algorithms for tasks like finding intersections and ordering geometric objects.
  - Multithreaded Sorting: Beneficial for parallel processing and multithreaded environments due to its divide-and-conquer 
  - approach that can be efficiently parallelized.

