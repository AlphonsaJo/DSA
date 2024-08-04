/*
1) Well-known algorithm used to find the maximum sum of a contiguous subarray within a one-dimensional array of numbers. 
2) It operates in linear time (making it efficient for large arrays). 
3) Iterates through the array and keeps track of the maximum subarray sum encountered up until then. 
*/ 
class Solution {
    public int maxSubArray(int[] nums) {
        int numSoFar = 0;
        int numMax = Integer.MIN_VALUE;

        for (int i = 0; i < nums.length; i++) {
            numSoFar += nums[i];

            if (numSoFar > numMax) {
                numMax = numSoFar;
            }

            if (numSoFar < 0) {
                numSoFar = 0;
            }
        }
        return numMax;
    }
}
