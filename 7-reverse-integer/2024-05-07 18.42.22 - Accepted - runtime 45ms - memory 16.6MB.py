class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        int_str = str(x)
        if int_str[0] == '-':
            int_str = int_str[1:]
            neg = True
        rng = range((-2)**(31), (2**31)-1)

        new_int_str = "".join([int_str[i] for i in range(len(int_str)-1, -1, -1)])
        new_int = int(new_int_str)
        if new_int not in rng:
            return 0
        elif neg:
            return -new_int
        else:
            return new_int
        