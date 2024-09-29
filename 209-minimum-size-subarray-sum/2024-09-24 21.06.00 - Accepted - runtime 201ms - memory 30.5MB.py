class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 1
        sm = nums[0]
        minln = len(nums) + 1
        while j <= len(nums):
            if sm >= target and j-i < minln:
                minln = j-i
            if sm > target and i < j-1:
                i += 1
                sm -= nums[i-1]
            elif sm < target:
                j += 1
                if j <= len(nums):
                    sm += nums[j-1]
            else:
                i += 1
                j += 1
                if i < len(nums):
                    sm -= nums[i-1]
                if j <= len(nums):
                    sm += nums[j-1]
        if minln == len(nums) + 1:
            return 0
        else:
            return minln