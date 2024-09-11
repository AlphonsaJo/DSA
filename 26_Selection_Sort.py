
'''

Points to note:
There are two nested loops: one to traverse the array and one to find the minimum element in the unsorted portion.
After finding the minimum, it swaps it with the first element of the unsorted portion.

Time and Space complexity
Best, Average, and Worst Case: O(n²) for all cases, as selection sort always performs the same number of comparisons.
O(1) since selection sort is an in-place sorting  At the start of each pass through the array (each iteration of the outer loop), we assume thealgorithm.

Q. Why initialize min_index = i inside the loop?: 
=> First element of the unsorted portion (which starts at index i) is the minimum. As we traverse the rest of the unsorted portion, we update min_index if we find a smaller element.


'''



def selection_sort(arr):
    n= len(arr)
    temp = 0
    for i in range(0, n):
        
        min_i = arr[i] #Assume
        for j in range(i+1, n):
          
            
            if arr[j] < arr[min_i]:  
                min_i = j 

        
        arr[i], arr[min_i] = arr[min_i], arr[i]
                
    return arr

arr = [9, 8, 7, 3]
print(selection_sort(arr))
