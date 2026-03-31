class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int l = 0;
        int[] ans = new int[temperatures.length];
        int r = 1;

        while(l < temperatures.length-1){
            if(temperatures[r] > temperatures[l]){
                ans[l] = r - l;
                l++;
                r = l + 1;
            }else{
                r++;
                if(r == temperatures.length){
                    l++;
                    r = l + 1;
                }
            }
        }
        return ans;
    }
}
