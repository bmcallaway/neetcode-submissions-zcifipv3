class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded = encoded + str(len(string)) + "#" + string
        return encoded
    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        i = 0
        while i < len(s):
            r = i
            while r < len(s) and s[r].isnumeric():
                r += 1
            length = int(s[i:r])
            start = r + 1
            end = start + length
            word = s[start:end]
            res.append(word)
            i = end
        return res