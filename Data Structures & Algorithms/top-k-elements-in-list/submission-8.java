class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> freq = new HashMap();
        for(int n : nums){
            freq.put(n, freq.getOrDefault(n, 0) + 1);
        }
        //1 2 2 3 3 3 4 4 4
        //1 - 1
        //2 - 2
        //3 - 3
        //4 - 3

        //4 - 3
        //3 - 3

        PriorityQueue<Map.Entry<Integer,Integer>> maxHeap = new PriorityQueue<>(
            (a, b) -> b.getValue() - a.getValue() 
        );
        for(Map.Entry<Integer, Integer> entry : freq.entrySet()){
            maxHeap.add(entry);
        }


        int[] res = new int[k];
        int idx = 0;

        while(idx < k){
            res[idx++] = maxHeap.poll().getKey();
        }
        return res;
    }
}
