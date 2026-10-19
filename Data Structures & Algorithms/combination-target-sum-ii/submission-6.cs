public class Solution {
    public List<List<int>> CombinationSum2(int[] candidates, int target) {
        List<List<int>> res = new();
        List<int> curr = new();
        int currSum = 0;
        Array.Sort(candidates);

        void dfs(int pos) {
            if(currSum == target) {
                res.Add(new List<int>(curr));
                return;
            }else if (currSum > target || pos >= candidates.Length) {
                return;
            }
            curr.Add(candidates[pos]);
            currSum += candidates[pos];
            dfs(pos + 1);
            currSum -= candidates[pos];
            curr.Remove(candidates[pos]);
            pos += 1;
            while (pos < candidates.Length && candidates[pos] == candidates[pos - 1]) {
                pos += 1;
            }
            dfs(pos);
        }
        dfs(0);
        return res;
    }

//                                  1 2 2 4 5 6 9
//                                      [1]
//                                   2      2 4 5 6 9
//                                [1, 2]    
//                               2     4 5 6 9
//                           [1, 2, 2]  
//                          4       5 6 9
//                         
}
