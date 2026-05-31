class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Freq = {}
        s2Freq = {}
        for letter in s1:
            s1Freq[letter] = s1Freq.get(letter, 0) + 1
        
        needed = len(s1Freq)
        matched = 0
        l, r = 0, 0

        while r < len(s2):
            letter = s2[r]
            s2Freq[letter] = s2Freq.get(letter, 0) + 1
            if letter in s1Freq and s1Freq[letter] == s2Freq[letter]:
                matched += 1
            length = r - l + 1
            if (length) > len(s1):
                letter = s2[l]
                s2Freq[letter] -= 1
                if letter in s1Freq and s1Freq[letter] - s2Freq[letter] == 1:
                    matched -= 1
                l += 1
            if matched == needed:
                return True
            r += 1
        return False
                
        



