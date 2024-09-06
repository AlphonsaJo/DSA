# DSA

https://www.geeksforgeeks.org/dsa-crash-course-interview-guide/

https://pomodoro-tracker.com/?category=Coding

![ASCII TABLE](https://github.com/user-attachments/assets/d78cc4c7-a1bd-441b-87a4-f29a91301c79)

<h1 style="font-family: Arial; color: darkslateblue;">Programming</h1>

<h2 style="font-family: Arial; color: coral;">1. Backtracking:</h2>

<p style="font-family: Georgia; font-size: 18px;">
<b>Q. What is Backtracking?</b><br><br>

<b>Ans:</b> <span style="color: black;">Backtracking</span> is a 
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


