class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Freq = [0] * 26
        s2Freq = [0] * 26

        l = 0
        r = len(s1)

        for let in s1:
            s1Freq[ord(let) - ord('a')] += 1

        for let in s2[:r]:
            s2Freq[ord(let) - ord('a')] += 1

        if s1Freq == s2Freq:
            return True

        while r < len(s2):
            s2Freq[ord(s2[r]) - ord('a')] += 1
            r += 1
            s2Freq[ord(s2[l]) - ord('a')] -= 1
            l += 1
            if s1Freq == s2Freq:
                return True
        return False