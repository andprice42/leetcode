class Solution:
    def reverseBits(self, n: int) -> int:
        bin_str = ""
        first_pass = True
        while n > 0:
            if first_pass:
                i = 0
                while 2**i <= n:
                    bin_str = "0" + bin_str
                    i += 1
                n -= 2**(i-1)
                bin_str = "1" + bin_str[1:]
                first_pass = False
            else:
                i = 0
                while 2**i <= n:
                    i += 1
                bin_str = bin_str[:len(bin_str)-i] + "1" + bin_str[len(bin_str)-i+1:]
                n -= 2**(i-1)
        while len(bin_str) < 32:
            bin_str = "0" + bin_str
        nval = 0
        k = 0
        for i in range(len(bin_str)):
            nval += (2**k)*int(bin_str[i])
            k += 1
        return nval