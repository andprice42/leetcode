class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i = 0
        while 2**i < n:
            i += 1
        return 2**i == n