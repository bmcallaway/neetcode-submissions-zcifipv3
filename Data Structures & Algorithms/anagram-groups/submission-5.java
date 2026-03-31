class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> anagrams = new HashMap();

        for(String s : strs){
            int[] count = new int[26];
            for(char c : s.toCharArray()){
                count[c - 'a']++;
            }
            String key = Arrays.toString(count);
            if(!anagrams.containsKey(key)){
                anagrams.put(key, new ArrayList());
            }
            anagrams.get(key).add(s);
        }
        return new LinkedList(anagrams.values());
    }
}
