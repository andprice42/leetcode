class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return self.dfs(candidates, target, [])
    def dfs(self, candidates: List[int], target: int, rsum: List[int]) -> List[List[int]]:
        ret_arr = []
        for c in candidates:
            nrsum = sum(rsum) + c
            if nrsum == target:
                rsum.append(c)
                rsum.sort()
                ret_arr.append(rsum)
            elif nrsum < target:
                nrsumarr = [i for i in rsum]
                nrsumarr.append(c)
                new_arrs = self.dfs(candidates, target, nrsumarr)
                if new_arrs:
                    [ret_arr.append(i) for i in new_arrs if i not in ret_arr]
            else:
                return ret_arr
        return ret_arr
