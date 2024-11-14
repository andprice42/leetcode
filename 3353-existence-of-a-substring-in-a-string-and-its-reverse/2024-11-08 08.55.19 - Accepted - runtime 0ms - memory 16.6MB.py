class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        l2strs = set()
        for i in range(1, len(s)):
            l2strs.add(s[i-1:i+1])
        for i in range(len(s)-2, -1, -1):
            pstr = s[i+1] + s[i]
            if pstr in l2strs:
                return True
        return False