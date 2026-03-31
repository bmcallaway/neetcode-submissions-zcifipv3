class Solution {
    public int calPoints(String[] operations) {
        Stack<Integer> scores = new Stack();
        for(String s : operations){
            if(s.equals("+")){
                int savedScore = scores.pop();
                int newScore = savedScore + scores.peek();
                scores.push(savedScore);
                scores.push(newScore);
            } else if(s.equals("D")){
                int newScore = scores.peek() * 2;
                scores.push(newScore);
            } else if (s.equals("C")){
                scores.pop();
            } else {
                scores.push(Integer.valueOf(s));
            }
        }
        int totalScore = 0;
        for(int n : scores){
            totalScore = totalScore + n;
        }
        return totalScore;
    }
}