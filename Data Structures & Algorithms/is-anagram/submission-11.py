class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sFreq = [0] * 26

        for letter in s:
            sFreq[ord(letter) - ord('a')] += 1
        
        for letter in t:
            sFreq[ord(letter) - ord('a')] -= 1

        for val in sFreq:
            if val != 0:
                return False
        
        return True