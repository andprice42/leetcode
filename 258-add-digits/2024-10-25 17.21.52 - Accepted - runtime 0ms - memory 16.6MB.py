class Solution:
    def addDigits(self, num: int) -> int:
        num_str = str(num)
        while len(num_str) > 1:
            sm = 0
            for i in num_str:
                sm += int(i)
            num_str = str(sm)
        return int(num_str)