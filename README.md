# DSA

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



<h1 style="font-family: Arial; color: darkslateblue;">Key Concepts</h1>

<h2 style="font-family: Arial; color: coral;">1. Backtracking:</h2>

<p style="font-family: Georgia; font-size: 18px;">

 <span style="color: black;">Backtracking</span> is a 
<span style="color: darkorange;"><b>general algorithmic technique</b></span> used to solve problems 
<span style="color: royalblue;">incrementally by trying out different possibilities</span> 
and <span style="color: red;">discarding those that don't meet the conditions</span>.

<br>
It is particularly useful for problems involving 
<span style="color: forestgreen;"><b>searching through a set of possibilities</b></span>, 
like puzzles, mazes, permutations, combinations, and constraint satisfaction problems.
</p>

<hr style="border: 2px solid coral; width: 90%;">

<h3 style="font-family: Arial; color: teal;">Key Applications:</h3>
<ul style="font-family: Verdana; font-size: 16px; padding-left: 20px;">
  <li style="color: teal;">Puzzle Solving</li>
  <li style="color: teal;">Mazes</li>
  <li style="color: teal;">Permutations</li>
  <li style="color: teal;">Constraint Satisfaction Problems</li>
</ul>

```python
def backtrack(solution, choices):
    if solution_is_complete(solution):
        process_solution(solution)
    else:
        for choice in choices:
            make_choice(choice)
            backtrack(solution, choices)
            undo_choice(choice)

```
<h2 style="font-family: Arial; color: coral;">2. BFS </h2>
 
- An algorithm for traversing or searching a graph or tree level by level, exploring all neighboring nodes before moving to the next level.

- Data Structure Used: BFS uses a queue to process nodes in the order they are discovered.

- Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges.

- Space Complexity: O(V), due to storage required for the queue and visited list.


Source: https://www.geeksforgeeks.org/dsa-crash-course-interview-guide/


