class MinStack {
    Stack<Integer> stack;
    Stack<Integer> minStack;
    public MinStack() {
        stack = new Stack();
        minStack = new Stack();
    }
    //min: -3 -2
    //sta: -3 -2 -2
    public void push(int val) {
        if(stack.isEmpty()){
            stack.push(val);
            minStack.push(val);
        }else{
            if(stack.peek() < val){
                stack.push(val);
            }else{
                if(minStack.peek() >= val){
                    minStack.push(val);
                }
                stack.push(val);
            }
        }
    }
    
    public void pop() {
        System.out.println("Min stack: ");
        for(int n : minStack){
            System.out.println(n);
        }
        System.out.println("Stack: ");
        for(int n : stack){
            System.out.println(n);
        }
        if(stack.peek().equals(minStack.peek())){
            stack.pop();
            minStack.pop();
        }else{
            stack.pop();
        }
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return minStack.peek();
    }
}
