public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
        Dictionary<int, int> freqs = new();

        foreach (var num in nums) {
            freqs[num] = freqs.GetValueOrDefault(num, 0) + 1;
        }

        List<int>[] buckets = new List<int>[nums.Length + 1];

        for (int i = 0; i < buckets.Length; i++) {
            buckets[i] = new List<int>();
        }

        foreach (var (key, val) in freqs) {
            buckets[val].Add(key);
        }

        int idx = 0;

        int[] result = new int[k];

        for (int i = buckets.Length - 1; i >= 0; i--) {
            foreach (var val in buckets[i]) {
                result[idx] = val;
                idx += 1;
                if (idx >= k) {
                    return result;
                }
            }
        }

        return result;
    }
}
