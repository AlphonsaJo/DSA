# Kadane's Algorithm 👨‍💻

1) Well-known algorithm used to find the ```maximum sum of a contiguous subarray``` within a ```one-dimensional array``` of numbers. 
2) It operates in ```linear time``` (making it efficient for large arrays). 
3) Iterates through the array and keeps track of the ```maximum subarray sum``` encountered up until then. 

## Applications
 - ```Temperature Analysis```: Finding periods with the highest average temperature increase.
 - ```Dynamic Programming```: Often used as a subroutine in more complex dynamic programming problems.
 - ```Genomics```: Identifying regions in DNA sequences with the highest similarity scores.
 - ```Feature Extraction```: In machine learning, it can be used for extracting significant features from time-series data.

## Key Components

  - ```numSoFar```: This variable keeps track of the sum of the current subarray being considered.
  - ```numMax```: This variable stores the maximum sum found so far. It is initialized to the smallest possible integer value to handle arrays that contain only negative numbers.
  - ```Loop```: The for loop iterates through each element in the array, updating the current sum (numSoFar) and checking if it exceeds the maximum sum (numMax). If numSoFar drops below zero, it is reset to zero, starting a new subarray from the next element.

## Time Complexity

  The time complexity of this solution is ```O(n)```, where nn is the length of the input array nums. This is because the algorithm only requires a single pass through the array.

## Space Complexity

  The space complexity is ```O(1)``` since only a constant amount of space is used for the variables numSoFar and numMax, regardless of the size of the input array.
