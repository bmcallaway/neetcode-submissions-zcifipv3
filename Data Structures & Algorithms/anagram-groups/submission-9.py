class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for s in strs:
            letters = [0] * 26
            for c in s:
                letters[ord(c) - ord('a')] += 1
            key = ""
            for n in letters:
                key = key,n
            if key not in map:
                map[key] = []
            print("letts[]",letters)
            print("key:",key)
            print("s:",s)
            map[key].append(s)
        
        res = []
        for list in map.values():
            print(list)
            res.append(list)
        return res



