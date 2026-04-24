class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        testList = []
        for word in strs:
            freq = [0]*26
            for let in word:
                freq[ord(let) - ord('a')] += 1
            key = str(freq)
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(word)

        res = []
        for anagram in anagrams.values():
            res.append(anagram)
        return res

        