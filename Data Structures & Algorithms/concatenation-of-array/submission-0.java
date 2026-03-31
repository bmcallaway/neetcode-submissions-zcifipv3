class Solution {
    public int[] getConcatenation(int[] nums) {
        int[] newNums = new int[nums.length*2];
        int l = 0;
        int r = nums.length;
        for(int n : nums){
            newNums[l] = n;
            newNums[r] = n;
            l++;
            r++;
        }
        return newNums;
    }
}