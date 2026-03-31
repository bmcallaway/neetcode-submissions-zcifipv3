class Solution {
    public int[] twoSum(int[] numbers, int target) {
        Map<Integer, Integer> indices = new HashMap();
        for(int i = 0; i < numbers.length; i++){
            int difference = target - numbers[i];
            if(indices.containsKey(difference)){
                if(indices.get(difference) < i){
                    return new int[] {indices.get(difference)+1, i+1};
                }else {
                    return new int[] {i+1, indices.get(difference)+1};
                }
            }else {
                indices.put(numbers[i], i);
            }
        }
        return null;
    }
}
