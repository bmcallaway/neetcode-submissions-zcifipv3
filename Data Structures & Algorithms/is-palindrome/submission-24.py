class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = ""
        for ltr in s:
            if ltr.isalnum():
                stripped = stripped + ltr.lower()
        
        print(stripped)

        l = 0
        r = len(stripped)-1

        while(l<r):
            if stripped[l] != stripped[r]: return False
            l += 1
            r -= 1
        return True