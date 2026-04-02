class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = [0] * 26
        s2Count = [0] * 26

        for letter in s1:
            s1Count[ord(letter) - ord('a')] += 1

        for letter in s2[:len(s1)]:
            s2Count[ord(letter) - ord('a')] += 1
        
        if s1Count == s2Count:
            return True
        
        l = 0
        r = len(s1)

        while r < len(s2):
            s2Count[ord(s2[r]) - ord('a')] += 1
            s2Count[ord(s2[l]) - ord('a')] -= 1
            if(s1Count == s2Count):
                return True
            r += 1
            l += 1

        return False
        