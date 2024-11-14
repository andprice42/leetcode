class Solution:
    def scoreOfString(self, s: str) -> int:
        sm = 0
        j = 1
        for i in range(len(s)-1):
            sm += abs(ord(s[i])-ord(s[j]))
            j += 1
        return sm