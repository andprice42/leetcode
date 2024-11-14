class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mx = 0
        cnt = 0
        i = 0
        while i < len(nums):
            while i < len(nums) and nums[i] == 1:
                cnt += 1
                i += 1
            mx = max(mx, cnt)
            cnt = 0
            i += 1
        return mx
            