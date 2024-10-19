class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = self.recurse(nums, {})
        mx = memo[len(nums)]
        if len(nums) > 1:
            memo = self.recurse(nums[1:], {})
            mx = max(mx, memo[len(nums)-1])
        return mx
    
    def recurse(self, nums: List[int], memo: dict) -> dict:
        if len(nums) <= 2:
            memo[len(nums)] = nums[0]
        else:
            if memo.get(len(nums) - 2) is None:
                m2 = self.recurse(nums[2:], memo)
                maxj = m2[len(nums) - 2]
            else:
                j2 = memo[len(nums) - 2]
                maxj = j2
            if len(nums) > 3 and memo.get(len(nums) - 3) is None:
                m3 = self.recurse(nums[3:], memo)
                maxj= max(maxj, m3[len(nums) - 3])
            elif len(nums) > 3:
                j3 = memo[len(nums) - 3]
                maxj = max(maxj, j3)
            memo[len(nums)] = maxj + nums[0]
        return memo