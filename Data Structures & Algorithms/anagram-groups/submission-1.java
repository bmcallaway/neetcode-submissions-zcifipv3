class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> anagrams = new HashMap();
        int[] chars = new int[26];
        for(String s : strs){
            chars = new int[26];
            for(char c : s.toCharArray()){
                chars[c - 'a']++;
            }
            String key = Arrays.toString(chars);

            if(!anagrams.containsKey(key)){
                anagrams.put(key, new LinkedList());
            }

            anagrams.get(key).add(s);
        }
        return new ArrayList<>(anagrams.values());
    }
}
