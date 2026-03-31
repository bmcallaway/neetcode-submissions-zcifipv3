class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        freq = {}
        freq['W'] = 0
        freq['B'] = 0

        for i in range(k):
            freq[blocks[i]] += 1
        
        l = 0
        r = k - 1

        ans = freq['W']

        while r+1 < len(blocks):
            freq[blocks[r+1]] += 1
            freq[blocks[l]] -= 1
            l += 1
            r += 1

            ans = min(ans, freq['W'])
        return ans
        