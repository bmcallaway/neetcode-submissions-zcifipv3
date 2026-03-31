class Solution {
    public int scoreOfString(String s) {
        int score = 0;
        char[] letters = s.toCharArray();
        for(int i = 1; i < s.length(); i++){
            if(letters[i] > letters[i-1]){
                score = score + letters[i] - letters[i-1];
            }else {
                score = score + letters[i-1] - letters[i];
            }
        }

        return score;
    }
}