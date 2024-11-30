# DSA

### A readme compiled by me consisting of notes on various DSA codes. 

Data structures are specialized formats for organizing and storing data, such as arrays, linked lists, stacks, and trees. Algorithms are step-by-step procedures or formulas for solving problems and performing tasks, like sorting and searching.

### Importance of DSA

   - Efficiency: Understanding DSA helps optimize the performance of programs, ensuring they run faster and use fewer resources.
   - Problem Solving: DSA provides a framework for solving complex problems methodically, making it easier to design effective solutions.
   - Scalability: Well-structured data can handle larger datasets and complex applications, which is essential in today's data-driven world.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 
| **Sorting Algorithm**   | **Best-Case Time Complexity** | **Average-Case Time Complexity** | **Worst-Case Time Complexity** | **Space Complexity** |
|-------------------------|-------------------------------|----------------------------------|---------------------------------|----------------------|
| **Bubble Sort**          | O(n)                          | O(n²)                            | O(n²)                           | O(1)                 |
| **Selection Sort**       | O(n²)                         | O(n²)                            | O(n²)                           | O(1)                 |
| **Insertion Sort**       | O(n)                          | O(n²)                            | O(n²)                           | O(1)                 |
| **Merge Sort**           | O(n log n)                    | O(n log n)                       | O(n log n)                      | O(n)                 |
| **Quick Sort**           | O(n log n)                    | O(n log n)                       | O(n²)                           | O(log n)             |
| **Heap Sort**            | O(n log n)                    | O(n log n)                       | O(n log n)                      | O(1)                 |
| **Counting Sort**        | O(n + k)                      | O(n + k)                         | O(n + k)                        | O(k)                 |
| **Radix Sort**           | O(nk)                         | O(nk)                            | O(nk)                           | O(n + k)             |
| **Bucket Sort**          | O(n + k)                      | O(n + k)                         | O(n²)                           | O(n)                 |
| **Shell Sort**           | O(n log n)                    | O(n log² n)                      | O(n log² n)                     | O(1)                 |
| **Tim Sort**             | O(n)                          | O(n log n)                       | O(n log n)                      | O(n)                 |
| **Tree Sort**            | O(n log n)                    | O(n log n)                       | O(n²)                           | O(n)                 |


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 1. Basic Data Structures
- **Stacks**
  - A collection of elements with Last-In-First-Out (LIFO) access.
  - Supports operations like push (add an item) and pop (remove the top item).

       <img src="https://github.com/user-attachments/assets/84effda8-3090-4be1-bd48-1578d8b7cca7" alt="stack" width="400" height="300" />

       *image source: https://fullyunderstood.com/stack/*

- **Queues**
  - A collection of elements with First-In-First-Out (FIFO) access.
  - Supports operations like enqueue (add an item) and dequeue (remove the front item).
  
## 2. Linear Data Structures
- **Arrays**
  - A collection of items stored in contiguous memory locations.
  - Allows fast access to elements using an index.
  
- **Linked Lists**
  - A collection of nodes, each containing data and a reference to the next node.
  - Supports dynamic size and efficient insertions/deletions.


      <img src = "https://github.com/user-attachments/assets/c45a3130-dd75-4099-a13e-8ffb0756e43e" alt="linked-list" width="400" height="150" />


## 3. Non-linear Data Structures
- **Trees**
  - A hierarchical structure with nodes, where each node has a value and references to child nodes.
  
  - **Binary Trees**: Each node has at most two children.
  
  - **Binary Search Trees (BST)**: Left child nodes are less than the parent node, right child nodes are greater.
    

      <img src = "https://github.com/user-attachments/assets/352f1d28-1b9c-4ddd-b492-f48d37e1dfe7" alt="BST" width="400" height="300" />
  
  *image source wikimedia commons*

  
  - **AVL Trees**: A self-balancing binary search tree that maintains balance by ensuring the heights of two child subtrees of any node differ by at most one.
    

     <!--  FOR AVL: <img src = "https://github.com/user-attachments/assets/acdfcfe9-0c52-443f-9bd0-73c70332ec16" alt="AVL" width="600" height="300" /> ''' -->

- **Graphs**
  - A collection of nodes (vertices) connected by edges.
  - Can be directed or undirected, weighted or unweighted.

## 4. Searching Algorithms
- **Linear Search**
  - A simple method to find an element by checking each item sequentially.
  
- **Binary Search**
  - An efficient method that requires a sorted array, dividing the search interval in half each time.

## 5. Sorting Algorithms
- **Merge Sort**
  - A divide-and-conquer algorithm that splits the array into smaller subarrays, sorts them, and merges them back together.
  
- **Quick Sort**
  - An efficient sorting algorithm that selects a 'pivot' and partitions the array into elements less than and greater than the pivot.

## 6. Graph Algorithms
- **Breadth-First Search (BFS)**
  - An algorithm that explores all neighbor nodes at the present depth prior to moving on to nodes at the next depth level.
  
- **Depth-First Search (DFS)**
  - An algorithm that explores as far as possible along a branch before backtracking.

## 7. Advanced Concepts
- **Dynamic Programming**
  - A method for solving complex problems by breaking them down into simpler subproblems, storing results to avoid redundant calculations.
  - Often used for optimization problems.
  
- **Greedy Algorithms**
  - A strategy that makes the locally optimal choice at each stage with the hope of finding a global optimum. It does not guarantee the optimal solution for all problems but is efficient for certain types.
 
    ![Greedy-search-path-example](https://github.com/user-attachments/assets/48cf442c-323f-4276-b67d-64f897bc48e3)



Source: https://www.geeksforgeeks.org/dsa-crash-course-interview-guide/


