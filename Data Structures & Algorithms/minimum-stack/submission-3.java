public class MinStack {
    Stack<Integer> stack;
    Stack<Integer> minStack;
    public MinStack() {
        minStack = new Stack();
        stack = new Stack();
    }
    
    public void push(int val) {
        stack.push(val);
        if(minStack.empty() || val <= minStack.peek()){
            minStack.push(val);
        }
    }
    
    public void pop() {
        int popped = stack.pop();
        if(popped == minStack.peek()){
            minStack.pop();
        }
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return minStack.peek();
    }
}
