class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_max = 0
        max_till_now = -inf
        for c in nums:
            cur_max = max(c, cur_max + c)
            max_till_now = max(max_till_now, cur_max)
        return max_till_now