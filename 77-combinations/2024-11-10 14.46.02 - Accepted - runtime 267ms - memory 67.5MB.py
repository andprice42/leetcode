class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret_arr = []
        for i in range(1, n-k+2):
            ret_arr = self.dfs(n, [i], k-1, ret_arr)
        return ret_arr
    
    def dfs(self, n: int, arr: List[int], k: int, ret_arr: List[List[int]]) -> List[List[int]]:
        if k == 0:
            ret_arr.append(arr)
            return ret_arr
        v = arr[-1]
        arr_cpy = [i for i in arr]
        for i in range(v+1, n+1):
            arr_cpy.append(i)
            ret_arr = self.dfs(n, arr_cpy, k-1, ret_arr)
            arr_cpy = arr_cpy[:-1]
        return ret_arr