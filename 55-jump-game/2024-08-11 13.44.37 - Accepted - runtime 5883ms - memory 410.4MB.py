class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = self.recurse(nums, {})
        can = memo[len(nums)]
        print(memo)
        return can
    
    def recurse(self, nums: List[int], memo: dict) -> dict:
        if memo.get(len(nums)):
            return memo
        if len(nums) <= 1:
            memo[len(nums)] = True
            return memo
        can = False
        i = 0
        jmp_rng = nums[0]
        for i in range(jmp_rng, 0, -1):
            memo = self.recurse(nums[i:], memo)
            can = memo[len(nums[i:])]
            if can:
                memo[len(nums)] = True
                return memo
            elif len(nums[nums[0]:]) > min(memo.keys()):
                j = 1
                cont = False
                for num in nums[1:nums[0] + 1]:
                    if len(nums[j + num:]) < min(memo.keys()):
                        cont = True
                        break
                    j += 1
                if cont is False:
                    memo[len(nums)] = False
                    return memo
        memo[len(nums)] = can
        return memo