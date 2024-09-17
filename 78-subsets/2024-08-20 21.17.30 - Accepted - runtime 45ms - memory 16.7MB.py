class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        arr = []
        ret_arr = [[]]
        for i in range(len(nums)):
            arr = [nums[i]]
            ret_arr = self.dfs(nums[i+1:], ret_arr, arr)
        return ret_arr

    def dfs(self, nums: List[int], ret_arr: List[List[int]], arr: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            ret_arr.append(arr)
            return ret_arr
        arr_cpy = [i for i in arr]
        for i in range(len(nums)):
            arr_cpy.append(nums[i])
            ret_arr = self.dfs(nums[i+1:], ret_arr, arr_cpy)
            arr_cpy = arr_cpy[:-1]
        ret_arr.append(arr_cpy)
        
        return ret_arr