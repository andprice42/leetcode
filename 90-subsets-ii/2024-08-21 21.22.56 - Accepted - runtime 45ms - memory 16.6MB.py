class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ret_arr = [[]]
        for i in range(len(nums)):
            ret_arr = self.dfs(nums[i:], ret_arr, [])
        return ret_arr
            
    def dfs(self, nums: List[int], ret_arr: List[List[int]], sub_arr: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            sub_arr.sort()
            if sub_arr not in ret_arr:
                ret_arr.append(sub_arr)
            return ret_arr
        else:
            sub_arr_cpy = [i for i in sub_arr]
            sub_arr_cpy.append(nums[0])
            for j in range(1, len(nums)):
                ret_arr = self.dfs(nums[j:], ret_arr, sub_arr_cpy)
            sub_arr_cpy.sort()
            if sub_arr_cpy not in ret_arr:
                ret_arr.append(sub_arr_cpy)
            return ret_arr