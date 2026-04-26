class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Freq = {}
        s2Freq = {}

        l = 0
        r = len(s1)

        for letter in s1:
            s1Freq[letter] = s1Freq.get(letter, 0) + 1

        for letter in s2[:r]:
            s2Freq[letter] = s2Freq.get(letter, 0) + 1
        
        if s1Freq == s2Freq:
            return True
        
        while r < len(s2):
            s2Freq[s2[r]] = s2Freq.get(s2[r], 0) + 1
            r += 1
            s2Freq[s2[l]] -= 1
            if s2Freq[s2[l]] == 0:
                s2Freq.pop(s2[l])
            l += 1
            print(s1Freq)
            print(s2Freq)
            if s1Freq == s2Freq:
                return True
        
        return False