class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ''.join(ch.lower() for ch in s if ch.isalnum())

        l = 0
        r = len(clean) - 1

        while l < r:
            if clean[l] != clean[r]:
                return False
            l += 1
            r -= 1
        return True
