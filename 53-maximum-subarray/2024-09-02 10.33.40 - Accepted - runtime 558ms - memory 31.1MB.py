class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # mx, memo = self.recurse(nums, mx, {}, (0, len(nums)))
        cur_max = 0
        max_till_now = -inf
        for c in nums:
            cur_max = max(c, cur_max + c)
            max_till_now = max(max_till_now, cur_max)
        return max_till_now

    # def recurse(self, nums: List[int], mx: int, memo: dict, rng: tuple) -> dict:
    #     if memo.get(rng) is None and rng[1] > rng[0]:
    #         start = rng[0]
    #         end = rng[1]
    #         if len(nums) == 1:
    #             memo[rng] = nums[0]
    #             mx = max(mx, nums[0])
    #             return mx, memo
    #         else:
    #             rng1 = (start, end-1)
    #             if memo.get(rng1) is None:
    #                 mx, memo = self.recurse(nums[:-1], mx, memo, rng1)
    #             rng2 = (start+1, end)
    #             if memo.get(rng2) is None:
    #             mx, memo = self.recurse(nums[1:], mx, memo, rng2)
    #             memo[rng] = memo[rng1] + nums[-1]
    #         mx = max(mx, memo[rng])
    #         return mx, memo
    #     else:
    #         return mx, memo