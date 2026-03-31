class Solution {
    public boolean isPalindrome(String s) {
        int l = 0;
        int r = s.length()-1;
        char[] letters = s.toLowerCase().toCharArray();
        while(l < r){
            while(l < r && !Character.isLetterOrDigit(letters[l])){
                l++;
            }
            while(l < r && !Character.isLetterOrDigit(letters[r])){
                r--;
            }
            if(l < r && letters[l] != letters[r]){
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
}
