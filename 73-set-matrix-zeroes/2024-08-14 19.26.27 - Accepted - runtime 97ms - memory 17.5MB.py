class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        hit_cols = set()
        hit_rows = set()
        for i in range(len(matrix)):
            hit_list = []
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    hit_rows.add(i)
                    hit_cols.add(j)
        
        for row in hit_rows:
            matrix[row] = [0 for i in range(len(matrix[0]))]
        for col in hit_cols:
            for i in range(len(matrix)):
                matrix[i][col] = 0
        return matrix

                
            
                
        