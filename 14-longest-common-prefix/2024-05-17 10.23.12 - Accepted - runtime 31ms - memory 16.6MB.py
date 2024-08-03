class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = ""
        prefs = set()
        prefs.add("")
        k = 0
        for s in strs:
            if k == 0:
                pref = s
            elif pref == s:
                continue
            else:
                diff = len(s)-len(pref)
                start = min(len(s), len(s)-diff)
                prev = len(pref)
                for i in range(start, -1, -1):
                    if s[:i] == pref[:i]:
                        pref = s[:i]
                        break
            k += 1
        return pref
                
        