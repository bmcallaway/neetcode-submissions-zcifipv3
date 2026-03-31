class Solution {
    public int longestConsecutive(int[] nums) {
        //2 20 4 10 3  4  5
        //2  3 4  4 5 10 20
        //2 3 4 5 10 20
        Set<Integer> uniqueNums = new HashSet();
        for(int n : nums){
            uniqueNums.add(n);
        }
        if(nums.length == 0){
            return 0;
        }
        int longestSequence = 0;
        for(int n : uniqueNums){
            if(!uniqueNums.contains(n-1)) {
                int length = 1;
                while(uniqueNums.contains(n + length)) {
                    length++;
                }
                if(length > longestSequence){
                    longestSequence = length;
                }
            }
        }

        return longestSequence;
    }
}
