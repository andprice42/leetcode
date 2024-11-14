class Solution:
    def isBalanced(self, num: str) -> bool:
        i = 0
        os = 0
        es = 0
        for n in num:
            if i % 2 == 1:
                os += int(n)
            else:
                es += int(n)
            i += 1
        return os == es