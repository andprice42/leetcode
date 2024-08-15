class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = self.recurse(obstacleGrid, {})
        if len(obstacleGrid) > 0 and len(obstacleGrid[0]) > 0 and obstacleGrid[0][0] == 1:
            return 0
        val = memo.get((len(obstacleGrid), len(obstacleGrid[0])))
        if val is None:
            return 0
        return val
    
    def recurse(self, obstacleGrid: List[List[int]], memo: dict) -> dict:
        if len(obstacleGrid) == 0:
            return memo
        elif memo.get((len(obstacleGrid), len(obstacleGrid[0])))is None:
            if len(obstacleGrid[0]) == 1 and len(obstacleGrid) == 1:
                memo[(1, 1)] = 1-obstacleGrid[0][0]
                return memo
            if len(obstacleGrid[0]) > 1 and obstacleGrid[0][1] == 0:
                memo = self.recurse([og[1:] for og in obstacleGrid], memo)
                num_rows = len(obstacleGrid)
                num_cols = len(obstacleGrid[0])
                v = memo.get((num_rows, num_cols-1))
                if v is None:
                    v = 0
                memo[(num_rows, num_cols)] = v

            if len(obstacleGrid) > 1 and obstacleGrid[1][0] == 0:
                memo = self.recurse(obstacleGrid[1:], memo)
                num_rows = len(obstacleGrid)
                num_cols = len(obstacleGrid[0])
                v = memo.get((num_rows-1, num_cols))
                if v is None:
                    v = 0
                if memo.get((num_rows, num_cols)):
                    memo[(num_rows, num_cols)] += v
                else:
                    memo[(num_rows, num_cols)] = v
            return memo
        else:
            return memo

        
        
