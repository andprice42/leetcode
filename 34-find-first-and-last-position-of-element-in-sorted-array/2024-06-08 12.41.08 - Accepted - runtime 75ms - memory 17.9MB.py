class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        arr = []
        if len(nums) == 0:
            return [-1,-1]
        ind = self.binSrch(nums, target-0.5, 0)
        if ind >= len(nums):
            return [-1,-1]
        elif nums[ind] == target:
            arr = [ind]
            bln = False
            for i in range(ind, len(nums)):
                if nums[i] != target:
                    bln = True
                    break
            if bln is False:
                arr = [ind, len(nums)-1]
            else:
                arr = [ind, i-1]
        if len(arr) == 0:
            return [-1,-1]
        return arr

    def binSrch(self, nums, t: int, botind: int) -> int:
        if len(nums) == 0:
            return botind
        mid = len(nums) // 2
        med = nums[mid]

        if med > t:
            return self.binSrch(nums[:mid], t, botind)
        else:
            if mid == 0:
                return self.binSrch(nums[mid+1:], t, botind+1)
            else:
                return self.binSrch(nums[mid+1:], t, botind+mid+1)