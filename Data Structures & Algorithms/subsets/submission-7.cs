public class Solution {
    public List<List<int>> Subsets(int[] nums) {
        List<List<int>> res = new();
        List<int> curr = new();
        void dfs(int pos) {
            if (pos >= nums.Length) {
                res.Add(new List<int>(curr));
                return;
            }
            curr.Add(nums[pos]);
            dfs(pos + 1);
            curr.Remove(nums[pos]);
            dfs(pos + 1);
        }
        dfs(0);
        return res;
    }
}
