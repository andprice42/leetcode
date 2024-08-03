class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ints = {"{}".format(i): i for i in range(10)}
        num1_int = 0
        k = 0
        for i in range(len(num1)-1, -1, -1):
            num1_int += (10**k)*ints.get(num1[i])
            k += 1
        k = 0
        num2_int = 0
        for j in range(len(num2)-1, -1, -1):
            num2_int += (10**k)*ints.get(num2[j])
            k += 1
        num3_int = num1_int * num2_int
        return str(num3_int)