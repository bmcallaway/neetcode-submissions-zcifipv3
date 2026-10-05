class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parentheses = ["(", ")"]
        freqs = {}
        res = []
        curr = ""
        def backtrack(pos):
            nonlocal res, curr, parentheses, freqs
            if freqs.get("(", 0) > n or freqs.get(")", 0) > freqs.get("(", 0):
                return
            if freqs.get("(", 0) == n:
                if freqs.get(")", 0) == freqs.get("(", 0):
                    res.append(curr[:])
                    return
            for parenthesis in parentheses:
                curr += parenthesis
                freqs[parenthesis] = freqs.get(parenthesis, 0) + 1
                backtrack(pos + 1)
                curr = curr[:-1]
                freqs[parenthesis] -= 1
        
        backtrack(0)
        return res

