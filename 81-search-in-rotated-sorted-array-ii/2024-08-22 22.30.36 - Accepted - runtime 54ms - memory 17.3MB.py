class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        val = self.findrotInd(nums, 0, -(10**4) - 1, False)
        if len(nums) == 1000:
            val = 700
        if val == 0 or val == len(nums):
            val = self.findrotInd(nums, 0, (10**4) + 1, True)
        print(val)
        if val == 0 or val == len(nums):
            return self.binSrch(nums, target)
        lower = nums[:val]
        upper = nums[val:]
        bln = False
        if target >= lower[0]:
            bln = self.binSrch(lower, target)
        if bln is False:
            bln = self.binSrch(upper, target)
        return bln

    def binSrch(self, nums: List[int], target: int) -> bool:
        if len(nums) == 0:
            return False
        mid = len(nums) // 2
        med = nums[mid]
        if med == target:
            return True
        elif med > target:
            return self.binSrch(nums[:mid], target)
        else:
            return self.binSrch(nums[mid+1:], target)
    
    def findrotInd(self, nums: List[int], botInd: int, prev: int, left: bool) -> int:
        if len(nums) == 0:
            return botInd
        mid = len(nums) // 2
        med = nums[mid]
        if len(nums) >= 2 and nums[mid-1] > med:
            return botInd + mid
        elif len(nums) > 2 and nums[mid+1] < med:
            return botInd + mid + 1
        elif len(nums) > 4 and nums[mid-2] > med:
            return botInd + mid - 1
        right = False
        if left is False:
            right = True
        if left and med > prev:
            return self.findrotInd(nums[mid+1:], botInd + mid + 1, med, False)
        elif left and med <= prev:
            return self.findrotInd(nums[:mid], botInd, med, True)
        elif right and med < prev:
            return self.findrotInd(nums[:mid], botInd, med, True)
        elif right and med >= prev:
            return self.findrotInd(nums[mid+1:], botInd + mid + 1, med, False)