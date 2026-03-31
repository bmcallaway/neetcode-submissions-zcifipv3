class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] ans = new int[nums.length];
        int product;
        for(int i = 0; i < nums.length; i++){
            product = 1;
            for(int j = 0; j < nums.length; j++){
                if(j != i){
                    product = product * nums[j];
                }
            }
            ans[i] = product;
        }
        return ans;
    }
}  
