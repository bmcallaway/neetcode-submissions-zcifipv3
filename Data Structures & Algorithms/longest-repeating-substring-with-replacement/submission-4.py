class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        longest = 1
        l = 0
        r = 0

        while r < len(s):
            window[s[r]] = window.get(s[r], 0) + 1
            r += 1
            while (r - l) - max(window.values()) > k:
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1
            longest = max(longest, r - l)

        return longest
            