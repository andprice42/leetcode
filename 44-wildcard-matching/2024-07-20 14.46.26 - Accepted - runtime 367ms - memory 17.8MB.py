class Solution:
    def equals(self, s: str, p: str):
        if len(s) != len(p):
            return False
        for i in range(len(s)):
            if s[i] != p[i] and p[i] != "?":
                return False
        return True

    def isMatch(self, s: str, p: str) -> bool:
        memo, ret = self.isMatchH(s, p, {})
        return ret

    def isMatchH(self, s: str, p: str, memo: dict):
        if len(s) == 0 and set(p) == set("*"):
            ret = True
        elif (len(s) == 0 and len(p) == 0):
            ret = True
        elif len(p) > 0 and len(s) > 0 and p[-1] not in ["*", "?"] and p[-1] != s[-1]:
            ret = False
        elif len(s) == 0:
            ret = False
        elif len(p) == 0:
            ret = False
        elif s[0] == p[0] or p[0] == "?":
            if memo.get((s[1:],p[1:])) is None:
                (memo, ret) = self.isMatchH(s[1:], p[1:], memo)
            else:
                ret = memo.get((s[1:],p[1:]))
            memo[(s, p)] = ret
            
        elif p[0] == "*":
            j = 0
            cnt = 0
            start = None
            end = None
            while j < len(p) and cnt < 2:
                if p[j] != "*" and cnt == 0:
                    start = j
                    cnt += 1
                elif cnt == 1 and p[j] == "*":
                    end = j
                    cnt += 1
                j += 1
            if start is None and j == len(p):
                ret = True
                memo[(s, p)] = True
                return (memo, ret)
            elif end is None and j == len(p):
                substr = p[start:]
            else:
                substr = p[start:end]

            if start > 1:
                p = p[start-1:]
            if end is None:
                delta = len(s)
            else:
                delta = end-start
            nmtch = False
            i = 0

            while i < len(s):
                if substr == s[i:(i+delta)]:
                    if memo.get((s[i:], p[1:])) is None:
                        memo, nmtch = self.isMatchH(s[i:], p[1:], memo)
                    else:
                        nmtch = memo.get((s[i:], p[1:]))
                elif "?" in substr and self.equals(s[i:(i+(delta))], substr):
                    if memo.get((s[i:], p[1:])) is None:
                        memo, nmtch = self.isMatchH(s[i:], p[1:], memo)
                    else:
                        nmtch = memo.get((s[i:], p[1:]))
                if nmtch:
                    memo[(s, p)] = True
                    ret = True
                    return (memo, ret)
                i += 1
            memo[(s, p)] = False
            ret = False
        else:
            memo[(s,p)] = False
            ret = False
        return (memo, ret)