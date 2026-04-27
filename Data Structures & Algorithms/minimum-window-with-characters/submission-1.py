class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        sFreq = {}
        tFreq = {}

        minLen = float("inf")
        longest = ""
        l = 0
        r = len(t)

        for let in t:
            tFreq[let] = tFreq.get(let, 0) + 1
        for let in s[:r]:
            sFreq[let] = sFreq.get(let, 0) + 1

        if self.contains(tFreq, sFreq):
            return s[:r]

        while r < len(s):
            sFreq[s[r]] = sFreq.get(s[r], 0) + 1
            r += 1
            while self.contains(tFreq, sFreq):
                length = r - l
                if length < minLen:
                    minLen = length
                    longest = s[l:r]
                sFreq[s[l]] -= 1
                l += 1

        return longest

    def contains(self, tFreq, sFreq):
        for let in tFreq:
            if let not in sFreq or sFreq[let] < tFreq[let]:
                return False
        return True