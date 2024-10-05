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


# Function to heapify a subtree rooted at index i
def heapify(arr, n, i):
    largest = i  
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child is larger than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  


        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build a maxheap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)


arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print("Sorted array is:", arr)



