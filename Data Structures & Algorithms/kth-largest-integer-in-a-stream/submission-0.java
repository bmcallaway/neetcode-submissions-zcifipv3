class KthLargest {
    int k = 0;
    int[] nums;
    public KthLargest(int k, int[] nums) {
        this.k = k;
        this.nums = nums;
        Arrays.sort(nums);
    }
    
    public int add(int val) {
        int[] copy = new int[nums.length+1];
        for(int i = 0; i < nums.length; i++){
            copy[i] = nums[i];
        }
        copy[copy.length-1] = val;

        nums = copy;

        Arrays.sort(nums);
        for(int i : nums){
            System.out.println("Nums: " + i);
        }
        int res = k;
        for(int i = nums.length - 1; i >= 0; i--){
            res--;
            if(res == 0){
                return nums[i];
            }
        }
        return -1;
    }
}
