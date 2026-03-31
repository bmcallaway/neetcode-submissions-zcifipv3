class Solution {
    public int[] productExceptSelf(int[] nums) {
        //1  2  4  6 nums
        //1  1  2  8 prefix
        //48 24 6  1 suffix
        int[] prefix = new int[nums.length];
        int[] suffix = new int[nums.length];
        int product = 1;
        for(int i = 0; i < nums.length; i++){
            prefix[i] = product;
            product = product * nums[i];
        }
        product = 1;
        for(int i = nums.length-1; i >= 0; i--){
            suffix[i] = product;
            product = product * nums[i];
        }
        for(int i = 0; i < nums.length; i++){
            nums[i] = prefix[i] * suffix[i];
        }
        return nums;
    }
}  
