class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}

        l = 0
        result = 0

        for r in range(len(s)):
            if s[r] not in freq:
                freq[s[r]] = 1
            elif s[r] in freq:
                while l < len(s) and s[r] in freq:
                    freq.pop(s[l])
                    #freq[s[l]] -= 1
                    l += 1
                freq[s[r]] = 1
            result = max(result, r - l + 1)

        return result