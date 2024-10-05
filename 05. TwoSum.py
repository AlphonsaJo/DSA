class Solution(object):
    def twoSum(self, nums, target):
        list = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    list = [i, j]
                else:
                    continue
        return list
