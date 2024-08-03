class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binSrch(nums, target, 0)
    
    def binSrch(self, nums: List[int], target: int, botind: int) -> int:
        print(nums)
        if len(nums) == 0:
            return botind
        mid = len(nums) // 2
        med = nums[mid]

        if med == target:
            return botind + mid
        elif med > target:
            return self.binSrch(nums[:mid], target, botind)
        else:
            return self.binSrch(nums[mid+1:], target, botind + mid + 1)

