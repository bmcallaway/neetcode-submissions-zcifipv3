public class Solution {
    public List<List<int>> CombinationSum(int[] nums, int target) {
        List<List<int>> res = new();
        List<int> curr = new();
        int currSum = 0;
        void dfs(int pos) {
            if (currSum == target) {
                res.Add(new List<int>(curr));
                return;
            }else if (currSum > target || pos >= nums.Length) {
                return;
            }
            curr.Add(nums[pos]);
            currSum += nums[pos];
            dfs(pos);
            currSum -= nums[pos];
            curr.Remove(nums[pos]);
            dfs(pos + 1);
        }

        dfs(0);
        return res;
    }

    //.             2 5 6 9
    //                 [2]
   //               2     5 6 9
   //             [2,2]    
   //            2     5 6 9
   //         [2,2,2]      [2,2,5]
   //        2     5 6 9 
   //     [2,2,2,2]
   //.   2     5 6 9 
 // x[2,2,2,2,2]x      
}
