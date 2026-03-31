class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> frequencies = new HashMap();
        for(int n : nums){
            frequencies.put(n, frequencies.getOrDefault(n, 0) + 1);
        }
        List<Integer>[] buckets = new List[nums.length+1];
        for(int i = 0; i < buckets.length; i++){
            buckets[i] = new ArrayList();
        }
        for(Map.Entry<Integer, Integer> entry : frequencies.entrySet()){
            buckets[entry.getValue()].add(entry.getKey());
        }
        int[] ans = new int[k];
        int idx = 0;
        for(int i = buckets.length-1; i > 0; i--){
            for(int n : buckets[i]){
                ans[idx] = n;
                idx++;
                if(idx == k){
                    return ans;
                } 
            }
        }
        return ans;
    }
}
