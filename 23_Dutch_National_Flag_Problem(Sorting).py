def sort_flag(arr):

    n = len(arr)

    low = 0; mid = 0; high = n - 1 # initialize low and mid pointers as 0 and high as the last index of array 

    while mid <= high:
        if arr[mid] == 0:

            arr[mid], arr[low] = arr[low], arr[mid]

            mid+=1

            low+=1

        elif arr[mid] == 1:

            mid+=1

        else:

            arr[high], arr[mid] = arr[mid], arr[high]

            high-= 1

            

    return arr
 
arr = [0, 1, 0, 2, 1, 2]

new_arr = sort_flag(arr)

print(new_arr)


 
