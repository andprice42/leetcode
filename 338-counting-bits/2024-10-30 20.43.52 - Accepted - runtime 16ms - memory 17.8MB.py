class Solution:
    def countBits(self, n: int) -> List[int]:
        lst = []
        s = []
        for i in range(n+1):
            if i == 0:
                lst.append(0)
                prev = 0
                s.append("0")
            elif i == 2**(len(s)-1):
                lst.append(1)
                prev = 1
                ["0" for j in range(len(s)-1)]
                s[-1] = "1"
            elif i % 2 != 0:
                lst.append(prev+1)
                prev += 1
                s[0] = "1"
            else:
                j = 0
                while j < len(s) and s[j] == "1":
                    s[j] = "0"
                    j += 1
                    prev -= 1
                if j > len(s)-1:
                    s.append("1")
                    prev = 0
                else:
                    s[j] = "1"
                prev += 1
                lst.append(prev)
        return lst
