class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        length = 0
        l = 0
        r = 0
        while r < len(s):
            count[ord(s[r]) - ord('A')] += 1

            while (r - l + 1) - max(count) > k:
                count[ord(s[l]) - ord('A')] -= 1
                l += 1

            length = max(length, r - l + 1)
            r += 1
        return length

