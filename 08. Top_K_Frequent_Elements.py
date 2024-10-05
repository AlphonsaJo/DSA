from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        cnt = Counter(nums)

        return [num for num, _ in cnt.most_common(k)]
          
