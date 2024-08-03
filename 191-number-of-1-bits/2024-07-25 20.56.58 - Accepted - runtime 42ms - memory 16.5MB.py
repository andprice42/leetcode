class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 0:
            return 0
        x = 0
        while 2**x <= n:
            x += 1
        x -= 1
        n -= 2**x
        if n > 0:
            cnt = 1 + self.hammingWeight(n)
        else:
            cnt = 1
        return cnt

        