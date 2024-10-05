class Solution(object):
    def missingNumber(self, nums):
        # Create a set from nums for O(1) lookups
        nums_set = set(nums)
        
        # Iterate over the expected range of numbers
        for num in range(len(nums) + 1):
            if num not in nums_set:
                return num
        
        # Return -1 if no missing number is found (should not happen)
        return -1

