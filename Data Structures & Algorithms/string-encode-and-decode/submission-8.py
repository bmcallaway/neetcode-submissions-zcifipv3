class Solution:

    def encode(self, strs: List[str]) -> str:
        #5Hello#5World
    #   5#Hello5#World
        encoded = ""
        for word in strs:
            encoded = encoded + str(len(word)) + "#" + word
        return encoded
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i in range(len(s)):
            j = i+1
            while s[j] != '#':
                j += 1
            print(i,j)
            length = int(s[i:j])
            print("length:",length)
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        print(res)
        return res




            
