class Solution:
    def romanToInt(self, s: str) -> int:
        val_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ln = len(s)
        sm = 0
        for i in range(ln):
            val = val_dict.get(s[i])
            if i + 1 < ln and val_dict.get(s[i+1]) > val:
                sm -= val
            else:
                sm += val
        return sm