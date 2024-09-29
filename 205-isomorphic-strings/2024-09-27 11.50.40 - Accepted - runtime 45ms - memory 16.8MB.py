class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        i = 0
        dct = {}
        tst = set()
        tqa = ""
        while i < len(s):
            v = dct.get(s[i])
            if v and v != t[i]:
                return False
            elif v is None and t[i] in tst:
                return False
            elif v is None:
                dct[s[i]] = t[i]
            tst.add(t[i])
            i += 1
        return True
