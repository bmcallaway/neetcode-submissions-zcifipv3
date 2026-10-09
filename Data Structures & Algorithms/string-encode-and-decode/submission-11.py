class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded = encoded + str(len(string)) + "#" + string
        print(encoded)
        return encoded
    def decode(self, s: str) -> List[str]:
        decoded = []
        l = 0
        while l < len(s):
            r = l + 1
            while s[r].isnumeric():
                r += 1
            length = int(s[l:r])
            l = r + 1
            r = l + length
            decoded.append(s[l:r])
            l = r
        return decoded

