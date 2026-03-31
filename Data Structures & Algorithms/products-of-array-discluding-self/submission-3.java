class Solution {
    public int[] productExceptSelf(int[] nums) {
        //[1   2  4  6]
        //[1   1  2  8]
        //[48  24 6  1]
        int[] prefix = new int[nums.length];
        int[] postfix = new int[nums.length];
        int product = 1;
        for(int i = 0; i < prefix.length; i++){
            prefix[i] = product;
            product = product * nums[i];
        }
        for(int n : prefix){
            System.out.println("prefix: " + n);
        }
        product = 1;
        for(int i = postfix.length-1; i >=0 ; i--){
            postfix[i] = product;
            product = product * nums[i];
        }
        for(int i = 0; i < nums.length; i++){
            nums[i] = prefix[i] * postfix[i];
        }
        return nums;
    }
}  
