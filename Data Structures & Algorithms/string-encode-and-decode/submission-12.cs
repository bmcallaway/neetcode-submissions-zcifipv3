public class Solution {

    public string Encode(IList<string> strs) {
        string encoded = "";

        foreach (var str in strs) {
            string length = str.Length.ToString();
            encoded = encoded + length + "#" + str;
        }
        return encoded;
    }

    public List<string> Decode(string s) {
        List<string> decoded = new();

        for (int i = 0; i < s.Length;) {
            int j = i;
            while (j < s.Length && char.IsDigit(s[j])) {
                j += 1;
            }
            int wordLength = int.Parse(s[i..j]);
            i = j + 1;
            j = i + wordLength;
            // 5#Hello5#World
            decoded.Add(s[i..j]);
            i = j;
        }
        return decoded;
   }
}
