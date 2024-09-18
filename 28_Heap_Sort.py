'''
#################
Time Complexity:
    Building the Heap: O(n), where n is the number of elements in the array.
    Heapify Operations: O(log n) per extraction, and since there are n elements, the total complexity for sorting is O(n log n).
Space Complexity: 
    Heap sort has a space complexity of O(1), meaning it sorts the array in-place without requiring additional storage beyond the input array.
Stability:
    Heap sort is not a stable sorting algorithm, meaning it does not necessarily preserve the relative order of equal elements.
    
####################
Types of Binary Heap:
A complete binary tree where each node satisfies the heap property:
    Max heap: parent node >= child nodes.
    Min heap: parent node <= child nodes.
    
######################
Key points:
n // 2 - 1:
    This is the index of the last non-leaf node in the binary heap.
range(n // 2 - 1, -1, -1):
    generates values from (n // 2 - 1) down to 0 (Middle arg: -1 is excluded) in reverse ( since step is-1)
    
######################
Note: 
Leaf nodes are already heaps by themselves (since they have no children) so you only need to start from the last non-leaf node and move upwards to the root.
This is more efficient than starting at the root.
'''



