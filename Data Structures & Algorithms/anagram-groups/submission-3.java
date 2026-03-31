class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> answers = new LinkedList();
        Map<String, List<String>> groups= new HashMap();
        for(String str : strs){
            int[] letterFreq = new int[26];
            for(char c : str.toCharArray()){
                letterFreq[c - 'a']++;
            }
            String key = Arrays.toString(letterFreq);
            if(groups.containsKey(key)){
                groups.get(key).add(str);
            }else{
                groups.put(key, new ArrayList());
                groups.get(key).add(str);
            }
            
        }

        for(Map.Entry<String, List<String>> entry : groups.entrySet()){
            System.out.println("Key: " + entry.getKey());
            for(String s : entry.getValue()){
                System.out.println("String: " + s);
            }
        }

        answers.addAll(groups.values());
        return answers;
    }
}
