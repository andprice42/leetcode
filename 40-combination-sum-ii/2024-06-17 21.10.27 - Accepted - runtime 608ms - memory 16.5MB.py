class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        if len(set(candidates)) == 1:
            i = 1
            while i <= len(candidates):
                if i*candidates[i-1] == target:
                    return [candidates[:i]]
                i += 1
            return None
        elif len(set(candidates)) == 2:
            ret_vals = []
            i = 0
            j = 1
            while i < len(candidates) and j < len(candidates)+1:
                if sum(candidates[i:j]) == target and candidates[i:j] not in ret_vals:
                    ret_vals.append(candidates[i:j])
                elif sum(candidates[i:j]) < target:
                    j += 1
                elif i == j:
                    j += 1
                else:
                    i += 1
            return ret_vals
                
        return self.dfs(candidates, target, [])
    def dfs(self, candidates: List[int], target: int, rsum: List[int]) -> List[List[int]]:
        if len(candidates) == 0:
            return None
        ret_vals = []
        memo = {}
        j = 0
        rsm = sum(rsum)
        for c in candidates:
            if c + rsm == target:
                nrsum = [i for i in rsum]
                nrsum.append(c)
                nrsum.sort()
                ret_vals.append(nrsum)
                return ret_vals
            elif c + rsm < target:
                nrsum = [i for i in rsum]
                nrsum.append(c)
                newcs = [candidates[k] for k in range(len(candidates)) if k != j]
                nrsums = self.dfs(newcs, target, nrsum)
                if nrsums:
                    [ret_vals.append(i) for i in nrsums if i not in ret_vals]
            else:
                return ret_vals
            j += 1
        return ret_vals
                
            