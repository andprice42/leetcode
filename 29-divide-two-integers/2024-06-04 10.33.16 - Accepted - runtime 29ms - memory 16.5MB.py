class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        divis = abs(divisor)
        divid = abs(dividend)
        if divis > divid:
            return 0
        str_divid = str(divid)
        ln = len(str_divid)
        i = 1
        str_sol = ""
        while len(str_divid) > 0 and i <= ln:
            val = int(str_divid[:i])
            if divis <= val:
                digit = 0
                sm = divis
                while sm <= val:
                    sm += divis
                    digit += 1
                str_sol += str(digit)
                sm -= divis
                val -= sm
                if val > 0:
                    str_divid = str(val) + str_divid[i:]
                    i = len(str(val))
                else:
                    str_divid = str_divid[i:]
                    i = 0
                i += 1
                ln = len(str_divid)
            else:
                str_sol += "0"
                i += 1

        sol = int(str_sol)
        
        if (divisor < 0 and dividend > 0) or (divisor > 0 and dividend < 0):
            if sol > 2147483648:
                return -2147483648
            return -sol
        else:
            if sol > 2147483647:
                return 2147483647
            return sol