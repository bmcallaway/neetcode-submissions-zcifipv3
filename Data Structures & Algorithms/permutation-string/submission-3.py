class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Freq = [0] * 26
        s2Freq = [0] * 26

        for letter in s1:
            s1Freq[ord(letter) - ord('a')] += 1

        for letter in s2[:len(s1)]:
            s2Freq[ord(letter) - ord('a')] += 1

        print("s1Freq:",s1Freq)
        print("s2Freq:",s2Freq)  
        if s1Freq == s2Freq: return True
        
        l = 0
        r = len(s1)
        while r < len(s2):
            s2Freq[ord(s2[l]) - ord('a')] -= 1
            l += 1
            s2Freq[ord(s2[r]) - ord('a')] += 1
            r += 1
            if s1Freq == s2Freq: return True

   
        return False