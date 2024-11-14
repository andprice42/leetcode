class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i = 0
        j = 0
        cookies = 0
        s.sort()
        g.sort()
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                cookies += 1
                i += 1
                j += 1
            else:
                j += 1
        return cookies