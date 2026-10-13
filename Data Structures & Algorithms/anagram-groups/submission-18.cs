public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        Dictionary<string, List<string>> anagrams = new();
        
        foreach (var str in strs) {
            int[] freq = new int[26];
            foreach (var c in str) {
                freq[(int)c - (int)'a'] += 1;
            }
            string key = string.Join(",", freq);
            if (!anagrams.ContainsKey(key)) {
                anagrams[key] = new List<string>();
            }
            anagrams[key].Add(str);
        }

        List<List<string>> res = new();

        foreach (var list in anagrams.Values) {
            res.Add(list);
        }
        return res;

    }
}
