# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        g = n // 2
        v = guess(g)
        upbnd = n
        lwrbnd = 1
        while v != 0:
            if v == 1:
                lwrbnd = g + 1
                g = (g + 1 + upbnd) // 2
            else:
                upbnd = g - 1
                g = (g - 1 + lwrbnd) // 2
            v = guess(g)
        return g