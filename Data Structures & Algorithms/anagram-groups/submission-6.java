class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> anagrams = new HashMap();
        List<List<String>> ans = new ArrayList();
        String key;

        for(String s : strs){
            int[] freq = new int[26];
            for(char c : s.toCharArray()){
                freq[c - 'a']++;
            }
            key = Arrays.toString(freq);
            if(anagrams.containsKey(key)){
                anagrams.get(key).add(s);
            }else {
                anagrams.put(key, new ArrayList());
                anagrams.get(key).add(s);
            }
        }

        for(List<String> list : anagrams.values()){
            ans.add(list);
        }

        return ans;
    }
}
