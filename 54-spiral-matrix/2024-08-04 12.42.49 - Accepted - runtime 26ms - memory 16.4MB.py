class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        memo = {}
        i = 0
        j = 0
        w = len(matrix[0])
        l = len(matrix)
        ret_arr = []
        right = True
        down = False
        left = False
        up = False
        while len(memo) < w*l:
            ret_arr.append(matrix[i][j])
            memo[(i,j)] = True
            if right:
                if memo.get((i,j+1)) or j+1 == w:
                    right = False
                    down = True
                    i = i + 1
                else:
                    j = j + 1
            elif left:
                if memo.get((i,j-1)) or j-1 < 0:
                    left = False
                    up = True
                    i = i - 1
                else:
                    j = j - 1
            elif down:
                if memo.get((i+1,j)) or i+1 == l:
                    down = False
                    left = True
                    j = j - 1
                else:
                    i = i + 1
            else:
                if memo.get((i-1,j)) or i - 1 < 0:
                    up = False
                    right = True
                    j = j + 1
                else:
                    i = i - 1
        return ret_arr
