class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        c = 0
        if n == 1:
            return True
        while True:
            c += 1
            if 2 ** c == n:
                return True
            if 2 ** c > n:
                return False