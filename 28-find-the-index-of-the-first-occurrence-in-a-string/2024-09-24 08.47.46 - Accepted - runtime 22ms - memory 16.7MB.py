class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ln = len(haystack)
        ndln = len(needle)
        if needle == haystack:
            return 0
        for i in range(ln-ndln+1):
            if haystack[i:ndln+i] == needle:
                return i
        return -1