class Solution {
    public int maxArea(int[] heights) {
        int l = 0;
        int r = heights.length-1;
        int max = 0;
        int volume = 0;
        while(l < r){
            if(heights[l] < heights[r]){
                volume = heights[l] * (r-l);
                l++;
            }else if(heights[l] >= heights[r]){
                volume = heights[r] * (r-l);
                r--;
            }
            max = Math.max(volume, max);
        }
        return max;
    }
}
