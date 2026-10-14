public class Solution {
    public bool IsPalindrome(string s) {
        int l = 0;
        int r = s.Length - 1;

        while (l < r) {
            if (!char.IsLetterOrDigit(s[l])) {
                l += 1;
            } else if (!char.IsLetterOrDigit(s[r])) {
                r -= 1;
            } else if (char.ToLower(s[l]) != char.ToLower(s[r])) {
                return false;
            } else {
                l += 1;
                r -= 1;
            }
        }

        return true;
    }
}
