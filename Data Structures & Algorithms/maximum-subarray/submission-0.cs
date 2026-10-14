public class Solution {
    public int MaxSubArray(int[] nums) {
        int l = 0;
        int r = 0;
        int sum = 0;
        int maxSum = nums[0];
        while (r < nums.Length) {
            sum += nums[r];
            maxSum = Math.Max(maxSum, sum);
            if (sum < 0) {
                sum = 0;
            }
            r += 1;
        }

        return maxSum;
    }
}
