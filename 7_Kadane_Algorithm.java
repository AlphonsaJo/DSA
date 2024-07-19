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
