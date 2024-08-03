class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        sm = 1
        nums = set(nums)
        while sm in nums:
            sm += 1
        return sm