class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        val = int("".join([str(i) for i in digits]))
        val += 1
        str_val = str(val)
        new_digs = [int(i) for i in str_val]
        return new_digs
        