class Solution {
    public int[] sortArray(int[] nums) {
        //9 10 1 1 1 2 3 1
        PriorityQueue<Integer> minHeap = new PriorityQueue();
        for(int n : nums){
            minHeap.add(n);
        }
        for(int i = 0; i < nums.length; i++){
            nums[i] = minHeap.poll();
        }
        return nums;
    }
}