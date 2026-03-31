class Solution {

    public String encode(List<String> strs) {
        String encoded = "";
        for(String s : strs){
            encoded = encoded + s.length() + '#' + s;
        }
        System.out.println("Encoded: " + encoded);
        return encoded;
    }

    public List<String> decode(String str) {
        List<String> decoded = new ArrayList();
        int i = 0;
        int j = 0;
        int length = 0;
        while(i < str.length()){
            j = i + 1;
            while(str.charAt(j) != '#'){
                j++;
            }
            length = Integer.parseInt(str.substring(i, j));
            System.out.println("length: " + length);
            //System.out.println(str.substring(j + 1, j + 1 + length));
            decoded.add(str.substring(j + 1, j + 1 + length));
            i = j + length + 1;
        }
        return decoded;
    }
}
