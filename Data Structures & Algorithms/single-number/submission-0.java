class Solution {
    public int singleNumber(int[] nums) {
        //11
        //10
        //11
        int ans = nums[0];
        //= 3
        /// 10
        //7 = 0111
        //6 = 0110
        //^ = 0001
        //6 = 0110
        //^ = 0111
        //7 = 0111
        //^ = 0000
        //8 = 1000
        //^ = 1000
        for(int i = 1; i < nums.length; i++){
            ans = nums[i] ^ ans;
        }
        return ans;
    }
}
