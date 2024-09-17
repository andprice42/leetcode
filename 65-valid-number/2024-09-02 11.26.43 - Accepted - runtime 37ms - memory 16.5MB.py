class Solution:
    def isNumber(self, s: str) -> bool:
        if s[0] in ['-', "+"]:
            s = s[1:]
        nums = set([str(i) for i in range(10)])
        if len(s) == 0 or s == "." or s[0] in ["e", "E"] or ".e" == s[0:2] or ".E" == s[0:2]:
            return False
        if "." in s:
            i = 0
            while s[i] != ".":
                if s[i] not in nums:
                    return False
                i += 1
            i += 1
            while i < len(s) and s[i] not in ["e", "E"]:
                if s[i] not in nums:
                    return False
                i += 1
            if i < len(s):
                i += 1
                if i == len(s):
                    return False
                elif s[i] in ["+", "-"]:
                    i += 1
                if i == len(s):
                    return False
                while i < len(s):
                    if s[i] not in nums:
                        return False
                    i += 1
        else:
            i = 0
            while i < len(s) and s[i] not in ["e", "E"]:
                if s[i] not in nums:
                    return False
                i += 1
            if i < len(s):
                i += 1
                if i == len(s):
                    return False
                elif s[i] in ["+", "-"]:
                    i += 1
                if i == len(s):
                    return False
                while i < len(s):
                    if s[i] not in nums:
                        return False
                    i += 1
        return True