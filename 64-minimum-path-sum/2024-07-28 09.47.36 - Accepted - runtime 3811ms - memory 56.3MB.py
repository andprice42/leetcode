class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = self.dynpro(grid, {})
        ln = len(grid)
        wd = len(grid[0])
        return memo[(ln-1, wd-1)]

    def dynpro(self, grid: List[List[int]], memo: dict[tuple: int]) -> dict[tuple: int]:   
        if len(grid) == 0 or len(grid[0]) == 0:
            return memo
        elif len(grid) == 1 and len(grid[0]) == 1:
            memo[(0, 0)] = grid[0][0]
        else:
            ln = len(grid)
            wd = len(grid[0])
            if len(grid[1:]) > 0 and memo.get((ln-2, wd-1)) is None:
                memo = self.dynpro(grid[1:], memo)
            if len(grid[0][1:]) > 0 and memo.get((ln-1, wd-2)) is None:
                ngrid = [row[1:] for row in grid]
                memo = self.dynpro(ngrid, memo)
            if memo.get((ln-2, wd-1)) is None:
                mn = memo[(ln-1, wd-2)]
            elif memo.get((ln-1, wd-2)) is None:
                mn = memo[(ln-2, wd-1)]
            else: 
                mn = min(memo[(ln-1, wd-2)], memo[(ln-2, wd-1)])
            memo[(ln-1, wd-1)] = mn + grid[0][0]
        return memo
