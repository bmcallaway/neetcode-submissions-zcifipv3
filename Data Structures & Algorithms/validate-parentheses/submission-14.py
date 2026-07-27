class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for bracket in s:
            if bracket == ']':
                if not stack or stack[-1] != '[':
                    return False
                else:
                    stack.pop()
            elif bracket == ')':
                if not stack or stack[-1] != '(':
                    return False
                else:
                    stack.pop()
            elif bracket == '}':
                if not stack or stack[-1] != '{':
                    return False
                else:
                    stack.pop()
            else:
                stack.append(bracket)

        if len(stack) > 0:
            return False
        return True
            