class Solution:
    def findComplement(self, num: int) -> int:
        bin_str = []
        n = num
        first_pass = True
        while n > 0:
            i = 0
            while 2**i <= n:
                if first_pass:
                    bin_str.append("0")
                i += 1
            first_pass = False
            if len(bin_str) == 0:
                bin_str.append("1")
            else:
                bin_str[i-1] = "1"
            n -= 2**(i-1)
        for j in range(len(bin_str)):
            if bin_str[j] == "0":
                bin_str[j] = "1"
            else:
                bin_str[j] = "0"
        sm = 0
        k = 0
        for i in range(len(bin_str)):
            sm += int(bin_str[i])*(2**k)
            k += 1
        return sm
