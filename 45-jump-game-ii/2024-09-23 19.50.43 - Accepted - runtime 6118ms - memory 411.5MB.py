class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = self.recjump(nums, {})
        return memo[max(1, len(nums)) - 1]
    
    def recjump(self, nums: List[int], memo: dict) -> dict:
        if len(nums) <= 1:
            memo[0] = 0
            return memo
        elif nums[0] == 0:
            memo[len(nums)-1] = -1
            return memo
        j = nums[0] + 1
        r = min(len(nums), j)
        k = len(nums) - 2
        mn = None
        for i in range(1, r):
            if memo.get(k) is None:
                memo = self.recjump(nums[i:], memo)

            if memo[k] >= 0 and mn is None:
                mn = memo[k] + 1
            elif memo[k] >= 0 and memo[k] + 1 < mn:
                mn = memo[k] + 1
            k -= 1
        if mn is None:
            memo[len(nums)-1] = -1
        else:
            memo[len(nums)-1] = mn
        return memo
