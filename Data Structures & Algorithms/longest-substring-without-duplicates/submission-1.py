class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)
        seen = set()
        l = 0
        r = 1
        seen.add(s[l])
        length = 1
        longest = length
        while r < len(s):
            if s[r] in seen:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
                    length -= 1
            seen.add(s[r])
            r += 1
            length += 1
            longest = max(longest, length)

        return max(length, longest)