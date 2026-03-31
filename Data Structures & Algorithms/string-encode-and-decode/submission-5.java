class Solution {

    public String encode(List<String> strs) {
        String res = "";
        for(String s : strs){
            res = res + s.length() + "#" + s;
        }
        System.out.println(res);
        return res;
    }
    //5#hello5#world
    public List<String> decode(String str) {
        List<String> res = new ArrayList();
        char[] word = str.toCharArray();
        int numberLength = 0;
        int countIdx = 0; 
        for(int i = 0; i < word.length;){
            countIdx = i; //= 0
            while(word[countIdx] != '#'){
                countIdx++;//= 1
            }
            int length = Integer.valueOf(str.substring(i, countIdx));
            res.add(str.substring(countIdx+1, countIdx+1+length));
            i = countIdx+1+length;
        }
        return res;
    }
}
