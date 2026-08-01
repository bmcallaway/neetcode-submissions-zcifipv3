class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = ""
        parentheses = ["(", ")"]
        openCount = 0
        closeCount = 0
        # (()
        def backtrack(i):
            nonlocal res, openCount, closeCount, parentheses, curr
            if openCount < closeCount:
                return
            if i == n*2:
                if openCount == n and closeCount == n:                        
                    res.append(curr)
                return
            for parenthesis in parentheses:
                if parenthesis == "(":
                    openCount += 1
                elif parenthesis == ")":
                    closeCount += 1
                curr = curr + parenthesis
                backtrack(i+1)
                curr = curr[:len(curr)-1]
                if parenthesis == "(":
                    openCount -= 1
                elif parenthesis == ")":
                    closeCount -= 1


        backtrack(0)

        return res
            
            