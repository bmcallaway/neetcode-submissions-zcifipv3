class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        while l < r:
            if not s[l].isalnum():
                print("s[l] not alpha")
                l += 1
                continue
            if not s[r].isalnum():
                print("s[r] not alpha")
                r -= 1
                continue
            if s[l].lower() == s[r].lower():
                print("s[l]:",s[l])
                print("s[r]:",s[r])
                l += 1
                r -= 1
            elif s[l].lower() != s[r].lower():
                return False
        return True
        