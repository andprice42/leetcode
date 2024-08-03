class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x is None:
            return False
        s = str(x)
        ln = len(s)
        if ln % 2 == 1:
            med = ln // 2
            j = med - 1
            for i in range(med+1, ln):
                if s[i] != s[j]:
                    return False
                j -= 1
        else:
            med2 = ln // 2
            med1 = med2-1
            j = med1
            for i in range(med2, ln):
                if s[i] != s[j]:
                    return False
                j -= 1
        return True