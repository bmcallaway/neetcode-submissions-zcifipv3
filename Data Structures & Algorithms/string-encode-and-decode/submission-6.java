class Solution {

    public String encode(List<String> strs) {
        //
        //5#hello5#world
        //012345678
        String encoded = "";
        for(String s : strs){
            encoded = encoded + s.length() + '#' + s;
        }
        return encoded;
    }

    public List<String> decode(String str) {
        List<String> decoded = new ArrayList();
        char[] encoded = str.toCharArray();
        for(int i = 0; i < str.length();i++){
            int r = i + 1;
            while(encoded[r] != '#'){
                r++;
            }
            int length = Integer.valueOf(str.substring(i, r));
            decoded.add(str.substring(r+1, r+1+length));
            i = r + length;
        }
        return decoded;
    }
}
