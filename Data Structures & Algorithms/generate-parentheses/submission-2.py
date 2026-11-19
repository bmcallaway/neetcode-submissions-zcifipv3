class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = ""
        parentheses = ["(", ")"]
        count = {}
        def dfs(pos):
            nonlocal curr, count
    
            if count.get("(", 0) > n or count.get(")", 0) > count.get("(", 0):
                return
            if count.get("(", 0) == n and count.get(")", 0) == n:
                res.append(curr[:])
                return
                
            for parenthesis in parentheses:
                curr += parenthesis
                count[parenthesis] = count.get(parenthesis, 0) + 1
                dfs(pos + 1)
                curr = curr[:-1]
                count[parenthesis] -= 1
        dfs(0)
        return res
        #       (
        #       (