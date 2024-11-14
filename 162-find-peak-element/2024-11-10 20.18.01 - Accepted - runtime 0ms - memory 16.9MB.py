class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return self.binSrch(nums, 0)
    def binSrch(self, nums: List[int], botInd: int) -> int:
        if len(nums) == 1:
            return botInd
        med = len(nums) // 2
        mid = nums[med]
        if len(nums) >= 3 and nums[med-1] < mid and nums[med+1] < mid:
            return botInd + med
        elif med > 0 and nums[med-1] > mid:
            return self.binSrch(nums[:med], botInd)
        elif len(nums) > 2 and nums[med+1] > mid:
            return self.binSrch(nums[med+1:], botInd+med+1)
        else:
            return botInd + med
