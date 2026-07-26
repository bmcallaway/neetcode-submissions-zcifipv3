class Solution:
    def minWindow(self, s: str, t: str) -> str:
        matched = 0
        minLen = float("inf")
        minSubString = ""
        print(minLen)
        tFreq = {}

        for letter in t:
            tFreq[letter] = tFreq.get(letter, 0) + 1
        
        needed = len(tFreq)

        sFreq = {}
        l, r = 0, 0
        while r < len(s):
            sFreq[s[r]] = sFreq.get(s[r], 0) + 1
            if s[r] in tFreq and sFreq[s[r]] == tFreq[s[r]]:
                matched += 1
            while matched == needed:
                length = r-l+1
                if length < minLen:
                    minSubString = s[l:r+1]
                    minLen = length
                sFreq[s[l]] -= 1
                if s[l] in tFreq and sFreq[s[l]] == tFreq[s[l]] - 1:
                    matched -= 1
                if sFreq[s[l]] == 0:
                    del sFreq[s[l]]
                l += 1
            r += 1
        return minSubString
                
            
        