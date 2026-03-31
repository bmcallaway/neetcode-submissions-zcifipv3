class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> freq = new HashMap();
        for(int n : nums) {
            freq.put(n, freq.getOrDefault(n, 0) + 1);
        }
        //[1 2 2 3 3 3]
        //[0 1 2 3 4 5 6]
        //[  1 2 3 ]
        List<Integer>[] buckets = new List[nums.length+1];
        for(int i = 0; i < buckets.length; i++){
            buckets[i] = new ArrayList<Integer>();
        }

        for(Map.Entry<Integer, Integer> entry : freq.entrySet()){
            buckets[entry.getValue()].add(entry.getKey());
        }

        //[0]
        //[1]
        //[2]
        //[3]
        int[] res = new int[k];
        int idx = 0;

        for(int i = buckets.length-1; i >= 0; i--){
            for(int n : buckets[i]){
                res[idx] = n;
                idx++;
                if(idx >= k){
                    return res;
                }
            }
        }
        return null;
    }
}
