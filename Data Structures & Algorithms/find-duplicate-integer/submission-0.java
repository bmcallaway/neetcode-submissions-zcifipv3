class Solution {
    public int findDuplicate(int[] nums) {
        Set<Integer> seen = new HashSet();
        for(int n : nums){
            if(seen.contains(n)){
                return n;
            }else{
                seen.add(n);
            }
        }
        return 0;
    }
}
