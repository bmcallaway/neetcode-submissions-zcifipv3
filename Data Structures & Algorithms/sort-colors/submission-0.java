class Solution {
    public void sortColors(int[] nums) {

        int[] buckets = new int[3];

        for(int n : nums){
            buckets[n]++;
        }
        //1 2 1
        int[] copy = new int[nums.length];

        int i = 0;
        for(int r = 0; r < buckets[0]; r++){
            nums[i] = 0;
            i++;
        }
        for(int w = 0; w < buckets[1]; w++){
            nums[i] = 1;
            i++;
        }
        for(int b = 0; b < buckets[2]; b++){
            nums[i] = 2;
            i++;
        }
        
    }
}