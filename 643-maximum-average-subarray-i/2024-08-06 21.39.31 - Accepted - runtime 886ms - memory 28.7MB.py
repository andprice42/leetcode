class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        end = k
        start = 0
        sm = sum(nums[0:k])
        mx = sm/k
        while end <= len(nums):
            nmx = sm/k
            if nmx > mx:
                mx = nmx
            sm -= nums[start]
            if end < len(nums):
                sm += nums[end]
            end += 1
            start += 1

        return mx