class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        current_vals = []

        result = 0
        for token in tokens:
            if token.lstrip('-').isnumeric():
                current_vals.append(token)
            else:
                #10 6 12
                val2 = current_vals.pop()
                val1 = current_vals.pop()
                match token:
                    case '+':
                        result = int(val1) + int(val2)
                    case '-':
                        result = int(val1) - int(val2)
                    case '/':
                        result = int(val1) / int(val2)
                    case '*':
                        result = int(val1) * int(val2)
                current_vals.append(result)

        return int(current_vals[-1])
                        
        