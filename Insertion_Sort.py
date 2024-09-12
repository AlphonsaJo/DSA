'''
Compare the current element with the elements in the sorted section (elements before it i.e. LHS) and shift those elements to the right 
until the correct position for the current element is found.

Outer loop - iterates through each element starting from index 1.
Inner loop - shifts elements of the sorted section to the right if they are larger than the current element.

Time and Space Complexity:
Best-case time complexity: O(n) - All elements are in their correct positions.
Worst-case time complexity: O(n^2) - All element are unsorted.
Average-case time complexity: O(n^2) - Elements are in random order and the time complexity will be quadratic in nature as well.
Space complexity: O(1) - In-place Sorting - does nor require additional space for sorting. 
''
