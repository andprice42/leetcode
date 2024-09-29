class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_cpy = [i for i in nums]
        nums_cpy.sort()
        for i in range(len(nums)):
            j = self.binSrch(nums_cpy[i+1:], i+1, target, nums_cpy[i])
            if j:
                vals = set([nums_cpy[i], nums_cpy[j]])
                break
        ret_arr = []
        for i in range(len(nums)):
            if nums[i] in vals:
                ret_arr.append(i)
            if len(ret_arr) == 2:
                return ret_arr
        return []
    def binSrch(self, nums: List[int], botInd: int, target: int, a: int) -> int:
        if len(nums) == 0:
            return None
        mid = len(nums) // 2
        med = nums[mid]
        if med + a == target:
            return botInd + mid
        elif med + a < target:
            return self.binSrch(nums[mid+1:], botInd + mid + 1, target, a)
        else:
            return self.binSrch(nums[:mid], botInd, target, a)
        