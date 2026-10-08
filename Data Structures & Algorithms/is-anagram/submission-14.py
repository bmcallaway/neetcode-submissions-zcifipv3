class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = [0] * 26
        
        for letter in s:
            freq[ord(letter) - ord('a')] += 1
        for letter in t:
            freq[ord(letter) - ord('a')] -= 1

        for val in freq:
            if val != 0:
                return False
        
        return True