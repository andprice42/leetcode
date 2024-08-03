class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ln = len(matrix)
        if ln == 0:
            return False
        med = ln // 2
        row = matrix[med]
        mid = len(row) // 2

        if row[mid] == target:
            return True
        elif row[mid] > target:
            nmx = matrix[:med]
            if len(row[:mid]) > 0:
                nmx.append(row[:mid])
            return self.searchMatrix(nmx, target)
        elif row[-1] < target:
            nmx = matrix[med+1:]
            return self.searchMatrix(nmx, target)
        else:
            nmx = [row[mid+1:]]
            return self.searchMatrix(nmx, target)
