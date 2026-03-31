class Solution {
    public void rotate(int[] nums, int k) {
        //   0 1 2 3 4 5 6 
        //   1 2 3 4 5 6 7
        //   i     k 
    //temp:  4 -3 
        int[] temp = new int[nums.length];
        for(int i = 0; i < temp.length; i++){
            if(k < nums.length){
                temp[k] = nums[i];
                k++;
            }else if(k == nums.length){
                k = 0;
                temp[k] = nums[i];
                k++;
            }else if(k > nums.length){
                k = k % nums.length;
                temp[k] = nums[i];
                k++;
            }

        }
        for(int i = 0; i < temp.length; i++){
            nums[i] = temp[i];
        }
    }
}