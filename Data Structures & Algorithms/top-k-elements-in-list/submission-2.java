class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> freq = new HashMap<>();
        for(int n : nums){
            freq.put(n, freq.getOrDefault(n, 0) + 1);
        }
        List<Integer>[] buckets = new List[nums.length+1];
        for(int i = 0; i < nums.length+1; i++){
            buckets[i] = new ArrayList();
        }

        for(Map.Entry<Integer, Integer> entry : freq.entrySet()){
            buckets[entry.getValue()].add(entry.getKey());
        }

        int[] res = new int[k];
        int idx = 0;
        for(int i = buckets.length-1; i >= 0; i--){
            for(int n : buckets[i]){
                System.out.println("N: " + n);
                res[idx++] = n;
                if(idx >= k){
                    return res;
                }
            }
        }
        return res;
    }
}
