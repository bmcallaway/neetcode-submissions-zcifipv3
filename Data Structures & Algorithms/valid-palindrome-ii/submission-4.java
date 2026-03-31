class Solution {
    public boolean validPalindrome(String s) {
        int l = 0;
        int r = s.length()-1;
        boolean deleted = false;
        while(l < r){
            if(s.charAt(l) == s.charAt(r)){
                l++;
                r--;
            }else {
                if(deleted){
                    System.out.println("Test1");
                    return false;
                }else {
                    if(isPalindrome(s.substring(l+1, r+1))){
                        l++;
                        deleted = true;
                    }else if(isPalindrome(s.substring(l, r))){
                        r--;
                        deleted = true;
                    }else {
                        System.out.println("Test2");
                        return false;
                    }
                }
            }
        }
        return true;
    }
    public boolean isPalindrome(String s){
        int l = 0;
        int r = s.length()-1;
        while(l < r){
            if(s.charAt(l) != s.charAt(r)){
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
}