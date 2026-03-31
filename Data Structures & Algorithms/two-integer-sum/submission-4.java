class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> contains = new HashMap();
        for(int i = 0; i < nums.length; i++){
            contains.put(nums[i], i);
        }

        for(int i = 0; i < nums.length; i++){
            if(contains.containsKey(target - nums[i]) && contains.get(target - nums[i]) != i){
                if(contains.get(target - nums[i]) < i){
                    return new int[] {contains.get(target - nums[i]), i};
                }else {
                    return new int[]{i, contains.get(target - nums[i])};
                }
            }
        }

        return null;
    }
}
