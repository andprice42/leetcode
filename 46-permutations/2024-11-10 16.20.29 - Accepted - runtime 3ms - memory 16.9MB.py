class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.dfs(nums, [], [])
    def dfs(self, nums: set(), perm: List[int], ret_vals: List[List[int]]) -> List[List[int]]:
        if len(nums) == 0:
            ret_vals.append(perm)
            return ret_vals
        numscpy = set([i for i in nums])
        permcpy = [i for i in perm]
        for i in nums:
            perm.append(i)
            numscpy.remove(i)
            ret_vals = self.dfs(numscpy, perm, ret_vals)
            numscpy.add(i)
            perm = [i for i in permcpy]
        
        return ret_vals