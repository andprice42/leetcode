class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        i = 0
        substr = ""
        while j < len(s) and i < len(t) and substr != s:
            stay = True
            while i < len(t) and stay:
                if s[j] == t[i]:
                    stay = False
                    substr += s[j]
                    j += 1
                    i += 1
                else:
                    i += 1
        if substr == s:
            return True
        return False

