class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tFreq = {}

        for letter in t:
            tFreq[letter] = tFreq.get(letter, 0) + 1
        
        matched, needed = 0, len(tFreq)

        l, r = 0, 0

        sFreq = {}

        minLen = float("inf")
        minString = ""
        while r < len(s):
            letter = s[r]
            sFreq[letter] = sFreq.get(letter, 0) + 1
            r += 1
            if letter in tFreq and sFreq[letter] == tFreq[letter]:
                matched += 1
            while matched == needed:
                length = (r - l) 
                if length < minLen:
                    minLen = length
                    minString = s[l:r]
                letter = s[l]
                if letter in tFreq and tFreq[letter] == sFreq[letter]:
                    matched -= 1
                sFreq[letter] -= 1
                l += 1
            
        return minString
