class Solution {
    public List<Integer> majorityElement(int[] nums) {
        int target = nums.length/3;
        Map<Integer, Integer> freq = new HashMap();
        for(int n : nums){
            freq.put(n, freq.getOrDefault(n, 0) + 1);
        }
        List<Integer> ans = new ArrayList<>();
        for(Map.Entry<Integer, Integer> entry : freq.entrySet()){
            if(entry.getValue() > target){
                ans.add(entry.getKey());
            }
        }
        return ans;
    }
}