class Solution {

    public String encode(List<String> strs) {
        String encoded = "";
        for(String s : strs){
            encoded = encoded + s.length() + "#" + s;
        }
        return encoded;
    }

    public List<String> decode(String str) {
        List<String> decoded = new LinkedList<>();
        String length = "";
        for(int i = 0; i < str.length(); i++){
            if(str.charAt(i) == '#'){
                String decodedWord = str.substring(i+1, i+1+Integer.valueOf(length));
                System.out.println("Decoded Word: " + decodedWord);
                decoded.add(decodedWord);
                i = i + Integer.valueOf(length);
                length = "";
            }else{
                length = length + str.charAt(i);
            }
        }
        return decoded;
    }
}
