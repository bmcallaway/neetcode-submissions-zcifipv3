class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        
        for string in strs:
            freq = [0] * 26
            for let in string:
                freq[ord(let) - ord('a')] += 1
            key = str(freq)
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(string)
        
        result = []

        
        return list(anagrams.values())