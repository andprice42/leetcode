class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        mp = {}
        for i in s:
            if mp.get(i):
                mp[i] += 1
            else:
                mp[i] = 1
        for c in t:
            if mp.get(c) is None:
                return c
            elif mp[c] == 1:
                del mp[c]
            else:
                mp[c] -= 1
        return None