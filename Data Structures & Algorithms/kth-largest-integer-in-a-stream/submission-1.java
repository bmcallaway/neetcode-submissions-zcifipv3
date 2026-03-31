class KthLargest {
    int test;
    PriorityQueue<Integer> maxHeap = new PriorityQueue(Comparator.reverseOrder());
    public KthLargest(int k, int[] nums) {
        test = k;
        for(int n : nums){
            maxHeap.add(n);
        }
    }
    
    public int add(int val) {
        maxHeap.add(val);
        //System.out.println("test:" + maxHeap.peek());
        List<Integer> savedNums = new ArrayList();
        //System.out.println("test1: " + maxHeap.poll());
        System.out.println("k: " + test);
        for(int i = 0; i < test-1; i++){
            savedNums.add(maxHeap.poll());
        }
        int kLargest = maxHeap.peek();
        for(int n : savedNums){
            maxHeap.add(n);
        }
        return kLargest;
    }
}
