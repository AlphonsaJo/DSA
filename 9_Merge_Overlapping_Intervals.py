class Solution(object):
    def merge(self, intervals):
    
        if not intervals:
            return []
    
        merged = []
        intervals.sort(key = lambda x:x[0])
    
        for interval in intervals:
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
        
            else:
                merged[-1][1] = max(interval[1], merged[-1][1])
        return merged

