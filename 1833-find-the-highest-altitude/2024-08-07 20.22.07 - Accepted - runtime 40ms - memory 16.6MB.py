class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        malt = 0
        calt = 0
        for e in gain:
            calt += e
            if calt > malt:
                malt = calt
        return malt
