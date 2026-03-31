class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Map<Integer, Integer> indices = new HashMap();
        for(int i = 0; i < nums.length; i++){
            if(indices.containsKey(nums[i])){
                int index = indices.get(nums[i]);
                if(Math.abs(index - i) <= k){
                    return true;
                }
                indices.put(nums[i], i);
            }else{
                indices.put(nums[i], i);
            }
        }
        return false;
    }
}