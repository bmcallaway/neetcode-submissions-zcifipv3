class Solution {
    public boolean isValid(String s) {
        if(s.length() % 2 != 0){
            return false;
        }
        Stack<Character> parenthesis = new Stack();
        for(char c : s.toCharArray()){
            if(c == '('){
                parenthesis.push(c);
            } else if(c == '['){
                parenthesis.push(c);
            } else if(c == '{'){
                parenthesis.push(c);
            } else if(c == ')'){
                if (parenthesis.size() > 0 && parenthesis.peek() == '('){
                    parenthesis.pop();
                } else{
                    return false;
                }
            } else if(c == ']'){
                if (parenthesis.size() > 0 && parenthesis.peek() == '['){
                    parenthesis.pop();
                } else{
                    return false;
                }
            } else if(c == '}'){
                if (parenthesis.size() > 0 && parenthesis.peek() == '{'){
                    parenthesis.pop();
                } else{
                    return false;
                }
            }
        }
        if(parenthesis.size() > 0){
            return false;
        }
        return true;
    }
}
