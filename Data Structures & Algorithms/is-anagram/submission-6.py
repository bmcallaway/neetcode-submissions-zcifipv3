class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        for letter in s:
            if(letter in count):
                count[letter] += 1
            else:
                count[letter] = 1
        for letter in t:
            if(letter in count):
                count[letter] -= 1
            else:
                count[letter] = 1
        for value in count.values():
            if value != 0:
                return False;
        return True;
        
