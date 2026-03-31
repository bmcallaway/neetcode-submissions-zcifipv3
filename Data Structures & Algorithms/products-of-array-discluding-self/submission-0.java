class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] preFix = new int[nums.length];
        int[] postFix = new int[nums.length];
        int[] results = new int[nums.length];
        if(nums.length <= 1){
            return nums;
        }
        preFix[0] = nums[0];
        for(int i = 1; i < nums.length; i++){
            preFix[i] =  nums[i] * preFix[i-1]; 
        }
        postFix[nums.length-1] = nums[nums.length-1];
        for(int i = nums.length-2; i >= 0; i--){
            postFix[i] = nums[i] * postFix[i+1];
        }
        results[0] = postFix[1];
        results[results.length-1] = preFix[results.length-2];
        for(int i = 1; i < nums.length-1; i++){
            results[i] = preFix[i-1] * postFix[i+1];
        }

        for(int i = 0;i < results.length; i++){
            System.out.println("Results[" + i + "]: " + results[i]);
        }

    return results;
    }
}  
