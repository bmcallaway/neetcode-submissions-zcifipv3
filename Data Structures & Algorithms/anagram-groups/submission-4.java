class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> anagrams = new HashMap();
        for(String s : strs){
            int[] freq = new int[26];
            for(char c : s.toCharArray()){
                freq[c - 'a']++;
            }
            String key = Arrays.toString(freq);
            
            if(!anagrams.containsKey(key)){
                anagrams.put(key, new ArrayList<String>());
            }
            anagrams.get(key).add(s);
        }
        List<List<String>> ans = new LinkedList();
        ans.addAll(anagrams.values());
        return ans;

    }
}
