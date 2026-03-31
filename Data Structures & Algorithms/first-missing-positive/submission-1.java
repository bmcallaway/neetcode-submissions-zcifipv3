class Solution {
    public int firstMissingPositive(int[] nums) {
        Set<Integer> seen = new HashSet<Integer>();
        for(int n : nums){
            if(!seen.contains(n)){
                seen.add(n);
            }
        }
        int min = 1;
        while(seen.contains(min)){
            min++;
        }
        return min;
    }
}