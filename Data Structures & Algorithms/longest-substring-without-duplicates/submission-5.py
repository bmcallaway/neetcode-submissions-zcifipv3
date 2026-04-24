class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        seen = set()
        l = 0
        r = 1
        seen.add(s[l])
        longest = 0
        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            longest = max(longest, len(seen))
            r += 1

        return longest