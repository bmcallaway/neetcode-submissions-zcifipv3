class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> ans = new ArrayList();
        Map<String, List<String>> anagrams = new HashMap();
        for(String s : strs){
            int[] frequencies = new int[26];
            for(char c : s.toCharArray()){
                frequencies[c - 'a']++;
            }
            String key = Arrays.toString(frequencies);
            if(!anagrams.containsKey(key)){
                anagrams.put(key, new ArrayList());
            }
            anagrams.get(key).add(s);
        }
        for(List<String> list : anagrams.values()){
            ans.add(list);
        }
        return ans;
    }
}
