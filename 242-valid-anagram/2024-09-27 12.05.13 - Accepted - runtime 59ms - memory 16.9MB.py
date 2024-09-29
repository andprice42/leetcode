class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dct = {}
        t_dct = {}
        i = 0
        while i < len(s):
            if s_dct.get(s[i]):
                s_dct[s[i]] += 1
            else:
                s_dct[s[i]] = 1
            
            if t_dct.get(t[i]):
                t_dct[t[i]] += 1
            else:
                t_dct[t[i]] = 1
            i += 1
        return s_dct == t_dct