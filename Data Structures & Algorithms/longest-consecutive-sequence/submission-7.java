class Solution {
    public int longestConsecutive(int[] nums) {
        //checking 2
        //if (1) 
        //length = length + 1
        //iterate to next num
        //else{
            //length = 1
        if(nums.length == 0){
            return 0;
        }
        Set<Integer> numbers = new HashSet();
        for(int n : nums){
            numbers.add(n);
        }
        //2 20 4 10 3 5
        int max = 0;
        for(int n : nums){
            int length = 1;
            while(numbers.contains(n-1)){
                length = length + 1;
                n = n-1;
            }
            if(length >= max){
                max = length;
            }
        }

        return max;
    }
}
