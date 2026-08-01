class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        res = []
        curr = []
        letters = {}
        letters["2"] = ["a", "b", "c"]
        letters["3"] = ["d", "e", "f"]
        letters["4"] = ["g", "h", "i"]
        letters["5"] = ["j", "k", "l"]
        letters["6"] = ["m", "n", "o"]
        letters["7"] = ["p", "q", "r", "s"]
        letters["8"] = ["t", "u", "v"]
        letters["9"] = ["w", "x", "y", "z"]
        def backtrack(i):
            nonlocal res, curr, letters
            if i >= len(digits):
                res.append("".join(curr))
                return
            for letter in letters[digits[i]]:
                curr.append(letter)
                backtrack(i+1)
                curr.pop()

        backtrack(0)
        return res