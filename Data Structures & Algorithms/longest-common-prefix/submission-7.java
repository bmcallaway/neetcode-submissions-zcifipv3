class Solution {
    public String longestCommonPrefix(String[] strs) {
        String longestPrefix = null;
        for(String s : strs){
            if(s == ""){
                return "";
            }
            if(longestPrefix == null){
                longestPrefix = s;
            }
            String currentPrefix = "";
            for(int i = 0; i < s.length() && i < longestPrefix.length(); i++){
                if(s.charAt(i) == longestPrefix.charAt(i)){
                    currentPrefix = currentPrefix + s.charAt(i);
                }else{
                    break;
                }
            }
            longestPrefix = currentPrefix;
        }
        return longestPrefix;
    }
}