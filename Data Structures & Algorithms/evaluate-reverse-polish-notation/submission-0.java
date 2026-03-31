class Solution {
    public int evalRPN(String[] tokens) {
        //1 2 3 4
        //= * -
        //5
        //
        Stack<Integer> numbers = new Stack();
        int prev = 0;
        for(String s : tokens){
            if(s.equals("+")){
                int val = numbers.pop();
                int val2 = numbers.pop();  
                numbers.push(val + val2);
            } else if(s.equals("-")){
                int val = numbers.pop();
                int val2 = numbers.pop();  
                numbers.push(val2 - val);
            } else if(s.equals("*")){
                int val = numbers.pop();
                int val2 = numbers.pop();  
                numbers.push(val2 * val);
            } else if(s.equals("/")){
                int val = numbers.pop();
                int val2 = numbers.pop();  
                numbers.push(val2 / val);
            } else{
                numbers.push(Integer.valueOf(s));
            }
        }
        return numbers.peek();
    }
}
