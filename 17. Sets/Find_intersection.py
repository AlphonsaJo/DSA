def find_common_elements(arr1, arr2):
    return list(set(arr1).intersection(set(arr2)))  # Find intersection of two sets, convert the result back to list iterable and return. 


num1 = [1, 2, 3, 4]
num2 = [3, 4, 5, 6]
common_elements = find_common_elements(arr1, arr2)
print("Common elements:", common_elements)
