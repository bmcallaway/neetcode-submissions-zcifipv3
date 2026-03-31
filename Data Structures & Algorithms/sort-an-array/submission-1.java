class Solution {
    public int[] sortArray(int[] nums) {
        //10 9 1 1 1 2 3 1
        // l r
        //9 10 1 1 1 2 3 1
        // l.  r
        //1 10 9 1 1 2 3 1
        //. l. r
        //1 9 10 1 1 2 3 1
        //  l    r
        //1 1 10 9 1 2 3 1
        //.   l  r
        for(int l = 0; l < nums.length-1; l++){
            for(int r = l + 1; r < nums.length; r++){
                if(nums[l] > nums[r]){
                    int temp = nums[r];
                    nums[r] = nums[l];
                    nums[l] = temp;
                }
            }
        }
        return nums;
    }
}