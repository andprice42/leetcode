class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        neg = False
        if len(s) == 0:
            return 0
        if s[0] == '-':
            neg = True
        
        if s[0] in ['-', '+']:
            s = s[1:]
        i = 0
        str_ints = [str(i) for i in range(0, 10)]

        while i < len(s) and s[i] in str_ints:
            i += 1

        s = s[:i]
        if s == '':
            return 0
        val = int(s)
        if neg:
            val = -val
        if val > ((2**31)-1):
            return ((2**31)-1)
        elif val < (-(2**31)):
            return (-(2**31))
        else:
            return val