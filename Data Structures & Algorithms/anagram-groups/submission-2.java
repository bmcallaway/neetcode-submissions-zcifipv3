class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> res = new LinkedList();
        Map<String, List<String>> groups = new HashMap();
        for(String s : strs){
            int[] count = new int[26];
            for(char c : s.toCharArray()){
                count[c - 'a']++;
            }
            String key = Arrays.toString(count);
            if(!groups.containsKey(key)){
                groups.put(key, new ArrayList());
            }

            groups.get(key).add(s);

        }

        res.addAll(groups.values());
        return res;
    }
}
