class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        ogmx = {}
        for i in range(n):
            for j in range(n):
                ogmx[(i, j)] = matrix[i][j]
        
        for i in range(n):
            for j in range(n):
                c = abs(n-1-i)
                r = j
                matrix[r][c] = ogmx[(i, j)]

