'''
Python code for finding duplicate elements in an array and returning the length of the array after removing them
'''

def remove_duplicates(nums):
    nums = list(set(nums))  # Convert to set for only storing unique elements, then back to list.
    return len(nums), nums  # Return length and modified array.


nums = [1, 1, 3, 5, 5, 5, 7]
length, new_array = remove_duplicates(nums)
print("Length after removing duplicates:", length)
print("Array after removing duplicates:", new_array)
