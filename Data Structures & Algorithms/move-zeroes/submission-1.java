class Solution {
    public void moveZeroes(int[] nums) {
        int l = 0;
        int r = 0;
        while(r < nums.length){
            if(nums[r] == 0){
                r++;
            }else{
                nums[l] = nums[r];
                r++;
                l++;
            }
        }
        while(l < nums.length){
            nums[l] = 0;
            l++;
        }
    }
}