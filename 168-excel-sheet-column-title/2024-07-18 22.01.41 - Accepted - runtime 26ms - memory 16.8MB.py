class Solution:
    import math
    def convertToTitle(self, columnNumber: int) -> str:
        abcs = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G',
    8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N',
    15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U',
    22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'}
        cn = columnNumber
        if cn <= 26:
            return abcs[cn]
        col = ""
        i = 0
        sm = 0
        while sm <= cn:
            sm += 26**i
            i += 1
        sm = int(round(sm, 0))
        sm -= 26**(i-1)
        sm -= 1
        i -= 1
        cn -= sm
        j = 0
        oi = i
        ogcn = cn
        while j < i:
            if j == i - 1:
                ind = ogcn % 26
            else:
                ind = int(math.ceil((cn/(26**oi))*26))
                cn -= int(((ind-1)/26)*(26**oi))
                oi -= 1
            if ind == 0:
                ind = 26
            col += abcs[ind]
            j += 1
        return col