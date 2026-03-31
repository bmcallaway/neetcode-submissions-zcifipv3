class Solution {
    public int lengthOfLongestSubstring(String s) {
        //zxyyxyz
        //l
        //z 
        Set<Character> seen = new HashSet();
        int l = 0;
        int r = 0;
        int max = 0;
        while(r < s.length()){
            if(!seen.contains(s.charAt(r))){
                seen.add(s.charAt(r));
                r++;
            }else{
                while(seen.contains(s.charAt(r))){
                    seen.remove(s.charAt(l));
                    l++;
                }
            }
            max = Math.max(max, r-l);
        }
        return max;
    }
}
