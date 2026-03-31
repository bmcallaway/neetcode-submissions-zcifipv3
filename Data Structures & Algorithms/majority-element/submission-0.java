class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer, Integer> freq = new HashMap();
        int target = nums.length/2;

        for(int n : nums){
            freq.put(n, freq.getOrDefault(n, 0) + 1);
        }
        for(Map.Entry<Integer, Integer> entry : freq.entrySet()){
            if(entry.getValue() > target){
                return entry.getKey();
            }
        }
        return 0;
    }
}