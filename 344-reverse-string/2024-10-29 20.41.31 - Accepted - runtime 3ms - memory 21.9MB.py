class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
            flip = s[i]
            flop = s[-i-1]
            s[i] = flop
            s[-i-1] = flip
            