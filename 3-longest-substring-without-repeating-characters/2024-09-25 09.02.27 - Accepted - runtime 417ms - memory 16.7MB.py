class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        maxln = 0
        while i < len(s):
            mp = {}
            while i < len(s) and s[i] not in mp.keys():
                mp[s[i]] = i
                i += 1
            ln = len(mp.keys())
            if ln > maxln:
                maxln = ln
            if i < len(s): 
                i = mp.get(s[i]) + 1
        return maxln

