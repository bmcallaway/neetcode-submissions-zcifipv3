class Solution {
    public boolean isValid(String s) {
        Stack<Character> brackets = new Stack();
        for(char c : s.toCharArray()){
            if(c == '[' || c == '{' || c == '('){
                brackets.push(c);
            }else if(brackets.empty()){
                return false;
            }else if(c == ']'){
                if(brackets.peek() == '['){
                    brackets.pop();
                }else{
                    return false;
                }
            }else if(c == '}'){
                if(brackets.peek() == '{'){
                    brackets.pop();
                }else{
                    return false;
                }
            }else if(c == ')'){
                if(brackets.peek() == '('){
                    brackets.pop();
                }else{
                    return false;
                }               
            }

        }

        if(!brackets.empty()){
            return false;
        }else{
            return true;
        }
    }
}
