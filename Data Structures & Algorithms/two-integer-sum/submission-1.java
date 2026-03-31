class Solution {
    public int[] twoSum(int[] nums, int target) {
        int diff;
        HashMap<Integer,Integer> seen = new HashMap();

        for(int i = 0; i < nums.length; i++){
            diff = target - nums[i];
            System.out.println("Diff: " + diff);
            if(seen.containsKey(diff)){
                int j = seen.get(diff);
                if(j < i){
                    return new int[] {j,i};
                }else{
                    return new int[] {i,j};
                }
            }else{
                seen.put(nums[i], i);
            }
        }

        return null;
    }
}
