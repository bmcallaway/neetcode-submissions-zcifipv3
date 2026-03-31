class Solution {
    public int maxArea(int[] heights) {
        //left pointer, right pointer = left pointer + 1
        //volume = smallerColumn height * (r - l)
        //if volume is greater than max volume
        int volume = 0;
        int max = 0;
        for(int i = 0; i < heights.length -1; i++){
            for(int j = i + 1; j < heights.length; j++){
                if(heights[i] < heights[j]){
                    volume = heights[i] * (j - i);
                }else if(heights[i] >= heights[j]){
                    volume = heights[j] * (j - i);
                }
                if(volume > max){
                    max = volume;
                }
            }
        }
        return max;
    }
}
