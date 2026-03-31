class Solution {
    public String mergeAlternately(String word1, String word2) {
        String res = "";
        int i = 0;
        for(i = 0; i < word1.length() && i < word2.length(); i++){
            res = res + word1.charAt(i) + word2.charAt(i);
        }
        while(i < word1.length()){
            res = res + word1.charAt(i);
            i++;
        }
        while(i < word2.length()){
            res = res + word2.charAt(i);
            i++;
        }

        return res;
        
    }
}