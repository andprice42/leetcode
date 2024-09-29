class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dct = {}
        for c in magazine:
            if dct.get(c):
                dct[c] += 1
            else:
                dct[c] = 1

        for d in ransomNote:
            if dct.get(d) is None or dct.get(d) == 0:
                return False
            dct[d] -= 1
        return True