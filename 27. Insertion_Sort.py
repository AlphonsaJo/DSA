'''
Compare elements to the left and shift elements to the right to insert element. 

Outer loop - iterates through each element starting from index 1.
Inner loop - shifts elements of the sorted section to the right if they are larger than the current element.

Time and Space Complexity:
Best-case time complexity: O(n) - All elements are in their correct positions.
Worst-case time complexity: O(n^2) - All element are unsorted. ~ i.e. decent with small datasets, bad with large datasets
Average-case time complexity: O(n^2) - Elements are in random order and the time complexity will be quadratic in nature as well.
Space complexity: O(1) - In-place Sorting - does nor require additional space for sorting. 
'''
def insertion_sort(arr):
    n = len(arr)
    
    for i in range(1, n):
        temp = arr[i]  
        j = i - 1
        
        
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        
       
        arr[j + 1] = temp
    
    return arr

arr = [2, 3, 4, 1, 8]
print(insertion_sort(arr))

