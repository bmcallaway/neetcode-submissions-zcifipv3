class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> freq = new HashMap<>();
        for(char c : s.toCharArray()){
            freq.put(c, freq.getOrDefault(c, 0) + 1);
        }
        for(char c : t.toCharArray()){
            freq.put(c, freq.getOrDefault(c, 0) - 1);
        }
        for(int n : freq.values()){
            if(n!=0){
                return false;
            }
        }        
        return true;
    }
}
