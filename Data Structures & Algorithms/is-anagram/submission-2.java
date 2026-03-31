class Solution {
    public boolean isAnagram(String s, String t) {
        int[] count = new int[26];
        
        for(char c : s.toCharArray()){
            count[c - 'a']++;
        }

        String key1 = Arrays.toString(count);
        count = new int[26];
        for(char c : t.toCharArray()){
            count[c - 'a']++;
        }

        if(key1.equals(Arrays.toString(count))){
            return true;
        }

        return false;
    }
}
