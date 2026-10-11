class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        length = 0
        l, r = 0, 0

        window = set()

        while r < len(s):
            while l < r and s[r] in window:
                window.remove(s[l])
                l += 1
                length -= 1
            window.add(s[r])
            r += 1
            length += 1
            longest = max(longest, length)

        return longest