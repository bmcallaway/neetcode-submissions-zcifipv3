class Solution {
    public int maxArea(int[] heights) {
        //left pointer, right pointer = left pointer + 1
        //volume = smallerColumn height * (r - l)
        //if volume is greater than max volume
        int volume = 0;
        int max = 0;
        int l = 0;
        int r = heights.length-1;
        while(l < r){
            if(heights[l] < heights[r]){
                volume = heights[l] * (r-l);
                l++;
            }else{
                volume = heights[r] * (r-l);
                r--;
            }
            if(volume > max){
                max = volume;
            }
        }
        return max;
    }
}
