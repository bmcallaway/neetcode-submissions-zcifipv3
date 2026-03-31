class Solution {
    public int[] twoSum(int[] numbers, int target) {
        Map<Integer, Integer> indices = new HashMap();

        for(int i = 0; i < numbers.length; i++){
            int difference = target-numbers[i];
            if(indices.containsKey(difference)){
                if(i+1 < indices.get(difference)){
                    return new int[]{i+1, indices.get(difference)};
                } else{
                    return new int[]{indices.get(difference), i+1}  ;                
                }

            }else {
                indices.put(numbers[i], i+1);
            }
        }
        return null;
    }
}
