class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dct = {}
        mns = set()
        for i in nums:
            if i in mns:
                mns.remove(i)
            else:
                mns.add(i)
        return mns.pop()
        