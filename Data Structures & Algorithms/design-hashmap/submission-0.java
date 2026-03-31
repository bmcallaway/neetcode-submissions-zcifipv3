class MyHashMap {
    int[] keyArray;
    public MyHashMap() {
        keyArray = new int[1000001];
        for(int i = 0; i < keyArray.length; i++){
            keyArray[i] = -1;
        }
    }
    
    public void put(int key, int value) {
        keyArray[key] = value;
    }
    
    public int get(int key) {
        int val = keyArray[key];
        if(val == -1){
            return -1;
        }
        return keyArray[key];
    }
    
    public void remove(int key) {
        keyArray[key] = -1;
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */