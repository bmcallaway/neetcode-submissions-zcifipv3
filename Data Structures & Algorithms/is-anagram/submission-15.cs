public class Solution {
    public bool IsAnagram(string s, string t) {
        int[] freqs = new int[26];

        foreach (var num in s) {
            freqs[(int)num - (int)'a'] += 1;
        }

        foreach (var num in t) {
            freqs[(int)num - (int)'a'] -= 1;
        }

        foreach (var num in freqs) {
            if (num != 0) {
                return false;
            }
        }
        return true;
    }
}
