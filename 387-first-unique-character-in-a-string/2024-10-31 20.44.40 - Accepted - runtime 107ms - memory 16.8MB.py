class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnts = {}
        for i in range(len(s)):
            if cnts.get(s[i]):
                cnts[s[i]] += 1
            else:
                cnts[s[i]] = 1
        for i in range(len(s)):
            if cnts.get(s[i]) == 1:
                return i
        return -1