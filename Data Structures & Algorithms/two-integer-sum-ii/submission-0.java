class Solution {
    public int[] twoSum(int[] numbers, int target) {
        Map<Integer, Integer> indices = new HashMap();

        for(int i = 0; i < numbers.length; i++){
            if(indices.containsKey(numbers[i])){
                return new int[]{indices.get(numbers[i]) + 1, i + 1};
            }else{
                indices.put(target - numbers[i], i);
            }

        }

        return null;
    }
}
