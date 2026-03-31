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
                anagrams.put(key, new LinkedList());
            }
            System.out.println(key);
            anagrams.get(key).add(s);
        }

        List<List<String>> result = new LinkedList();

        for(Map.Entry<String, List<String>> entry : anagrams.entrySet()){
            result.add(entry.getValue());
        }

        return result;
    }
}
