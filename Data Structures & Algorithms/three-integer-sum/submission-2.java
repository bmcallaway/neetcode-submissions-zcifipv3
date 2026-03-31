class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> ans = new ArrayList();
        Arrays.sort(nums);
        //-4 -1 -1 0 1 2
        for(int i = 0; i < nums.length-2; i++){
            int l = i + 1;
            int r = nums.length-1;
            if(nums[i] > 0){
                break;
            }
            if(i > 0 && nums[i] == nums[i-1]){
                continue;
            }
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
                    while(l < r && nums[l-1] == nums[l]){
                        l++;
                    }
                }
            }
        }
        return ans;
    }
}
