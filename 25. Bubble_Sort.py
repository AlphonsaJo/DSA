def bubble_sort(arr):
    n = len(arr)
    # Outer loop for entire array
    # Inner loop to compare adjacent elements
    # reduce inner loop range to avoid unecessary comparisons by excluding already sorted elements
    # Worst, Best and Average Case - O(n^2) - non-optimized version w/o 'swapped' flag variable
    # Space Complexity - O(1)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr


arr = [3, 2, 8, 0]
sorted_arr = bubble_sort(arr)
print("Sorted array = ", sorted_arr)

