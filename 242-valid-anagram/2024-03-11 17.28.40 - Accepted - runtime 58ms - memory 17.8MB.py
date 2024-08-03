class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sarr = [i for i in s]
        tarr = [i for i in t]
        sarr.sort()
        tarr.sort()
        if sarr == tarr:
            return True
        else:
            return False