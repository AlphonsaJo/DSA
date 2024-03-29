class Solution(object):
    def merge(self, nums1, m, nums2, n):
        
        # Initialize pointers for nums1 and nums2
        i = m - 1
        j = n - 1
        # Initialize pointer for the merged array at the end of nums1
        k = m + n - 1
        
        # Merge elements from the end
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If there are remaining elements in nums2, copy them to nums1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
