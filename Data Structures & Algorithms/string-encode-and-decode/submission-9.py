class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for string in strs:
            encodedString = encodedString + str(len(string)) + '#' + string
        return encodedString
    def decode(self, s: str) -> List[str]:
        #       5#hello5#world
        decodedStrings = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] != '#':
                j += 1
            wordLen = int(s[i:j])
            start = j + 1
            end = start + wordLen
            decodedStrings.append(s[start:end])
            i = end

        return decodedStrings
        
