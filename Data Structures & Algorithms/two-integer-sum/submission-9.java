class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> indices = new HashMap();
        int difference;

        for(int i = 0; i < nums.length; i++){
            difference = target - nums[i];
            if(indices.containsKey(difference)){
                return new int[] {indices.get(difference), i};
            }else{
                indices.put(nums[i], i);
            }
        }
        return null;
    }
}
