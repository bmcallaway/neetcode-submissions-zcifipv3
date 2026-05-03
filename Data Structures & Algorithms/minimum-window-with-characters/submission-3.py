class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tFreq = {}
        sFreq = {}

        minimum = ""
        minLen = float("inf")
        
        for let in t:
            tFreq[let] = tFreq.get(let, 0) + 1
        
        needed = len(tFreq)
        matched = 0

        l = 0
        for r, letter in enumerate(s):
            sFreq[letter] = sFreq.get(letter, 0) + 1
            if letter in tFreq and tFreq[letter] == sFreq[letter]:
                matched += 1
            while matched == needed:
                currentLen = r - l + 1
                if currentLen < minLen:
                    minLen = currentLen
                    minimum = s[l:r+1]
                if s[l] in tFreq and tFreq[s[l]] == sFreq[s[l]] and (tFreq[s[l]] - 1) < sFreq[s[l]]:
                    matched -= 1
                sFreq[s[l]] -= 1
                l += 1
        return minimum





