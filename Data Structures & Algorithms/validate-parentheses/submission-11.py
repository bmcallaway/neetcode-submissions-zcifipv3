class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        
        for bracket in s:
            match bracket:
                case '[':
                    brackets.append(bracket)
                    print("added [")
                case '{':
                    brackets.append(bracket)   
                case '(':
                    brackets.append(bracket)
                case ']':
                    if len(brackets) == 0 or brackets.pop() != '[':
                        return False
                case '}':
                    if len(brackets) == 0 or brackets.pop() != '{':
                        return False
                case ')':
                    if len(brackets) == 0 or brackets.pop() != '(':
                        return False 
        
        if len(brackets) == 0:
            return True
        return False