class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> seen = new HashMap();

        char[] sArray = s.toCharArray();
        char[] tArray = t.toCharArray();

        for(char c : sArray){
            if(seen.containsKey(c)){
                seen.put(c, seen.getOrDefault(c, 0)+1);
            }else{
                seen.put(c, 1);
            }
        }

        for(char c : tArray){
            if(seen.containsKey(c)){
                seen.put(c, seen.getOrDefault(c, 0)-1);
            }else{
                seen.put(c, 1);
            }
        }

        for(int n : seen.values()){
            if(n>0){
                return false;
            }
        }
        return true;
    }
}
