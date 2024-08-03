class Solution:
    def addBinary(self, a: str, b: str) -> str:
        asum = 0
        bsum = 0
        k = 0
        for i in range(len(a)-1, -1, -1):
            asum += (2**k)*int(a[i])
            k += 1
        
        k = 0
        for j in range(len(b)-1, -1, -1):
            bsum += (2**k)*int(b[j])
            k += 1
        c = asum + bsum
        if c == 0:
            return "0"
        x = 0
        bin_arr = []
        first = True
        while 2**(x-1) <= c:
            if 2**x > c:
                first = False
                bin_arr[x-1] = "1"
                c -= 2**(x-1)
                x = 0
            elif 2**x == c:             
                if first:
                    bin_arr.append("1")
                    first = False
                else:
                    bin_arr[x] = "1"

                c -= 2**x
                x = 0
            elif first:
                bin_arr.append("0")
            x += 1

        rev = [bin_arr[i] for i in range(len(bin_arr)-1, -1, -1)]
        ret = "".join(rev)
        return ret