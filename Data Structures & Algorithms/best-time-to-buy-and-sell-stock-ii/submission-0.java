class Solution {
    public int maxProfit(int[] prices) {
        int l = 0;
        int r = 1;
        int total;
        if(prices.length == 1){
            return 0;
        }
        int sum = 0;
        int profit = 0;
        while(r < prices.length){
            if(prices[r] > prices[l]){
                profit = prices[r] - prices[l];
                sum = sum + profit;
            }else{
                l = r;
                l--;
            }
            l++;
            r++;
        }
        return sum;
    }
}