class Solution:
    def minWindow(self, s: str, t: str) -> str:
        shortest = ""
        shortLen = float("inf")

        tFreq = {}
        window = {}

        for let in t:
            tFreq[let] = tFreq.get(let, 0) + 1

        need = len(tFreq)
        matched = 0

        l = 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in tFreq and window[s[r]] == tFreq[s[r]]:
                matched += 1
            while matched == need:
                length = r - l + 1
                if length < shortLen:
                    shortLen = length
                    shortest = s[l:r+1]
                if s[l] in tFreq and window[s[l]] >= tFreq[s[l]] and window[s[l]] - 1 < tFreq[s[l]]:
                    matched -= 1
                window[s[l]] -= 1
                l += 1

        return shortest