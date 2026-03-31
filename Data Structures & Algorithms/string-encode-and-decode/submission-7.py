class Solution:

    def encode(self, strs: List[str]) -> str:
        response = ""
        for s in strs:
            response = response + str(len(s)) + '#' + s
        return response
        
    #3#ten

    def decode(self, s: str) -> List[str]:
        print("s:",s)
        answer = []
        i = 0
        while i < len(s):
            j = i
            while(s[j].isdigit()):
                j += 1
            length = int(s[i:j])
            answer.append(s[j+1: j+length+1])
            i = j+length+1
        return answer
