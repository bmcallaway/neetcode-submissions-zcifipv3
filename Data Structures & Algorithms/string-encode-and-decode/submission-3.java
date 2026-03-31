class Solution {

    public String encode(List<String> strs) {
        String encoded = "";

        for(String s : strs){
            encoded = encoded + s.length() + "#" + s;
        }
        return encoded;
    }

    public List<String> decode(String str) {
        List<String> decoded = new LinkedList();
        char[] encoded = str.toCharArray();
        String length = "";
        int lenVal = 0;
        for(int i = 0; i < encoded.length;){
            if(encoded[i] == '#'){
                i++;
                lenVal = Integer.valueOf(length);
                int j = 0;
                String decodedWord = "";
                while(j < lenVal){
                    decodedWord = decodedWord + encoded[i];
                    i++;
                    j++;
                }
                decoded.add(decodedWord);
                length = "";
            }else{
                length = length + encoded[i];
                i++;
            }
        }

        return decoded;

    }
}
