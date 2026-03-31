class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> ans = new ArrayList();
        // 0  1  2 3 4 5
        //-4 -1 -1 0 1 2
        // i  l        r
        //sum = -3
        // i     l     r
        //sum = -3
        // i       l   r
        //sum = -2
        // i         l r
        //sum = -1
        //    i  l     r
        //sum =  0
        int l;
        int r;
        for(int i = 0; i < nums.length-2; i++){
            if (nums[0] > 0) break;
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            l = i + 1;
            r = nums.length-1;
            while(l < r){
                int sum = nums[i] + nums[l] + nums[r];
                if(sum < 0){
                    l++;
                }else if(sum > 0){
                    r--;
                }else if(sum == 0){
                    List<Integer> triplet = new ArrayList();
                    triplet.add(nums[i]);
                    triplet.add(nums[l]);
                    triplet.add(nums[r]);
                    ans.add(triplet);
                    l++;
                    r--;
                    while(l < r && nums[l] == nums[l-1]) {
                        l++;
                    }
                }
            }
        }
        return ans;
    }
}
