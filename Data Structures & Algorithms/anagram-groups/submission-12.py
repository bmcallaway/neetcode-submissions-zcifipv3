class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        anagrams = {}
        for word in strs:
            freq = [0] * 26
            for c in word:
                freq[ord(c) - ord('a')] += 1
            key = str(freq)
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(word)

        for anagram in anagrams.values():
            result.append(anagram)
        
        return result
        
