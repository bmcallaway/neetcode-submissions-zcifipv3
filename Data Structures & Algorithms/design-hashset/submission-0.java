class MyHashSet {
    int M = 1334;
    List<Integer>[] buckets = new List[M];
    public MyHashSet() {
        for(int i = 0; i < M; i++){
            buckets[i] = new LinkedList();
        }
    }
    
    public void add(int key) {
        if(!contains(key)){
            int index = key % M;
            buckets[index].add(key);
        }
    }
    
    public void remove(int key) {
        int index = key % M;
        buckets[index].remove(Integer.valueOf(key));
    }
    
    public boolean contains(int key) {
        int index = key % M;
        return buckets[index].contains(key);
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * boolean param_3 = obj.contains(key);
 */