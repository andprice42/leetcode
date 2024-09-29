class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cntdict = {}
        n = len(nums)
        for e in nums:
            if cntdict.get(e) is None:
                cntdict[e] = 1
            else:
                cntdict[e] += 1
            
            if cntdict[e] > (n // 2):
                return e
        return e