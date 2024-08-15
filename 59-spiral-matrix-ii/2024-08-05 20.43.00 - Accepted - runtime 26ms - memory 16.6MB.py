class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        memo = {}
        i = 0
        j = 0
        right = True
        down = False
        left = False
        up = False
        v = 1
        mx = [[0 for k in range(n)] for l in range(n)]
        while len(memo) < n**2:
            mx[i][j] = v
            memo[(i,j)] = True
            if right:
                if memo.get((i,j+1)) or j+1 == n:
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
                if memo.get((i+1,j)) or i+1 == n:
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
            v += 1
        return mx