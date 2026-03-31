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
        int currentMax = 1;
        for(int n : uniqueNums){
            while(uniqueNums.contains(n+1)){
                System.out.println("currentMax: " + currentMax);
                System.out.println("n: " + n);
                currentMax++;
                n = n+1;
            }
            if(currentMax > longestSequence){
                longestSequence = currentMax;
            }
            currentMax = 1;
        }

        return longestSequence;
    }
}
