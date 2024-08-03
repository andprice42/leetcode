class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return [v for k, v in self.dfs(nums, [], {}).items()]
    def dfs(self, nums: List[int], perm: List[int], ret_map: dict) -> dict:
        if len(nums) == 0 and "".join([str(i) for i in perm]) not in ret_map.keys():
            ky = "".join([str(i) for i in perm])
            ret_map[ky] = perm
            return ret_map
        
        permcpy = [i for i in perm]
        for n in range(len(nums)):
            numscpy = [nums[i] for i in range(len(nums)) if i != n]
            perm.append(nums[n])
            ret_map = self.dfs(numscpy, perm, ret_map)
            perm = [i for i in permcpy]
        
        return ret_map

