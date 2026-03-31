class Solution {
    public String longestCommonPrefix(String[] strs) {
        String longestPrefix = null;
        int idx = 0;
        for(String s : strs){
            if(s.equals("")){
                return "";
            }
            if(longestPrefix == null){
                longestPrefix = s;
            }
            String currentPrefix = "";
            idx = 0;
            while(idx < longestPrefix.length() && idx < s.length()){
                if(s.charAt(idx) == longestPrefix.charAt(idx)){
                    currentPrefix = currentPrefix + s.charAt(idx);
                }else{
                    break;
                }
                idx++;
            }
            longestPrefix = currentPrefix;
        }
        return longestPrefix;
    }
}