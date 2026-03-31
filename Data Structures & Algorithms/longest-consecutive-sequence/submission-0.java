class Solution {
    public int longestConsecutive(int[] nums) {
        int max = 0;
        Set<Integer> numSet = new HashSet();

        for(int n : nums){
            numSet.add(n);
        }

        int length;

        for(int n : numSet){
            length = 1;
            if(!numSet.contains(n - 1)){
                while(numSet.contains(n + length)){
                    length++;
                }
                if(length > max){
                    max = length;
                }
            }
        }

        return max;
    }
}
