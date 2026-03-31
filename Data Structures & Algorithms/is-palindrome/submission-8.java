class Solution {
    public boolean isPalindrome(String s) {
        int l = 0;
        int r = s.length()-1;
        char[] letters = s.toLowerCase().toCharArray();
        while(l < r){
            while(l < letters.length && !Character.isLetterOrDigit(letters[l])){
                l++;
            }
            while(r > 0 && !Character.isLetterOrDigit(letters[r]) && r >= 0){
                r--;
            }
            System.out.println("L: " + l);
            System.out.println("R: " + r);
            if(l >= letters.length || r < 0){
                break;
            }
            if(letters[l] != letters[r]){
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
}
