class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_cpy = []
        ind_map = {}
        for i in range(len(nums)):
            nums_cpy.append(nums[i])
            if ind_map.get(nums[i]):
                ind_map[nums[i]].append(i)
            else:
                ind_map[nums[i]] = [i]
        nums_cpy.sort()
        for i in range(len(nums)):
            j = self.binSrch(nums_cpy[i+1:], i+1, target, nums_cpy[i])
            if j and nums_cpy[i] != nums_cpy[j]:
                ret_arr = [ind_map[nums_cpy[i]][0], ind_map[nums_cpy[j]][0]]
                ret_arr.sort()
                return ret_arr
            elif j:
                ret_arr = [ind_map[nums_cpy[i]][0], ind_map[nums_cpy[j]][1]]
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
        