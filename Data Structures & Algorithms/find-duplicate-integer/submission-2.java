class Solution {
    public int findDuplicate(int[] nums) {
        boolean[] seen = new boolean[10001];
        for(int n : nums){
            if(seen[n]){
                return n;
            }else{
                seen[n] = true;
            }
        }
        return 0;
    }
}
