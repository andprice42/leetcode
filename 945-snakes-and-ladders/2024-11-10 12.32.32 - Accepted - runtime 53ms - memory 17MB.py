class lnde:
    def __init__(self, val: tuple, next: Optional['lnde'] = None):
        self.val = val
        self.next = next

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        fq = lnde((n-1, 0, True, 0))
        tail = fq
        cnt = 1
        visited = set()
        while fq:
            curr = (fq.val[0], fq.val[1])
            if curr in visited:
                fq = fq.next
                continue
            else:
                visited.add(curr) 
            num = self.getNumber(fq.val, n)
            for nm in range(num+1, min(num+7, n**2 + 1)):
                loc = self.getBoardLoc(nm, n)
                jump = (loc[0], loc[1], loc[2], fq.val[3]+1)
                # consider snake or ladder
                if board[jump[0]][jump[1]] != -1:
                    loc = self.getBoardLoc(board[jump[0]][jump[1]], n)
                    jump = (loc[0], loc[1], loc[2], fq.val[3]+1)
                # win if going left
                if jump[0] == 0 and jump[2] is False and jump[1] == 0:
                    return jump[3]
                # win if going right
                elif jump[0] == 0 and jump[2] is True and jump[1] == n-1:
                    return jump[3]
                tail.next = lnde(jump)
                tail = tail.next
            fq = fq.next
        return -1

    def getNumber(self, vals: tuple, n: int) -> int:
        i = vals[0]
        j = vals[1]
        right = vals[2]
        row = (n-1) - i
        if right:
            val = (row*n) + j + 1
        else:
            val = (row*n) + (n-j)
        return val

    def getBoardLoc(self, val: int, n: int) -> tuple:
        r = val // n
        if r == val/n:
            r -= 1
        right = (r % 2 == 0)
        row = n-1-r
        if right and val % n == 0:
            c = n - 1
        elif right:
            c = (val % n) - 1
        elif val % n == 0:
            c = 0
        else:
            c = n - (val % n)
        return (row, c, right)
