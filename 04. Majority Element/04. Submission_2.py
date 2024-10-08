'''
Iterating over set(nums) avoids counting the same element multiple times.
Using // ensures an integer result for the majority constraint.
'''
class Solution(object):
    def majorityElement(self, nums):
        constraint = len(nums) // 2
        max_list = []
        for i in set(nums):
            if nums.count(i) > constraint:
                max_list.append(i)
                unique_list = list(set(max_list))
        return max(unique_list)
