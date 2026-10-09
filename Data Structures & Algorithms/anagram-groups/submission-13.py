class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for string in strs:
            freq = [0] * 26
            for c in string:
                freq[ord(c) - ord('a')] += 1
            key = str(freq)
            if key not in groups:
                groups[key]  = []
            groups[key].append(string)

        res = []
        for key, val in groups.items():
            res.append(val)
        return res
