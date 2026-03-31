class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] res = new int[2];
        Map<Integer, Integer> indices = new HashMap();

        for(int i = 0; i < nums.length; i++){
            int difference = target - nums[i];
            if(indices.containsKey(difference)){
                return new int[] {indices.get(difference), i};
            }else{
                indices.put(nums[i], i);
            }
        }
        return null;
    }
}
