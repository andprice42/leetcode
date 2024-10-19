class lnde:
    def __init__(self, val: tuple, next: Optional['lnde'] = None):
        self.val = val
        self.next = next

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visit = set()
        for i in range(1, len(board)-1):
            for j in range(1, len(board[0])-1):
                if board[i][j] == 'O':
                    visit.add((i, j))

        visited = set()
        while len(visit) > 0:
            i, j = visit.pop()
            visited.add((i, j))
            hit_set = set()
            hit_set.add((i, j))
            tpl = self.getNbs(board, (i, j), visited)
            head = tpl[0]
            tail = tpl[1]
            hit = True
            while head:
                tpl = head.val
                i = tpl[0]
                j = tpl[1]
                if tpl in visited:
                    head = head.next
                    continue
                visited.add(tpl)
                if tpl in visit:
                    visit.remove(tpl)
                if i == 0 or j == 0 or i == len(board)-1 or j == len(board[0])-1:
                    hit = False
                else:
                    hit_set.add((i, j))
                tpl = self.getNbs(board, (i, j), visited)
                if tpl[0]:
                    tail.next = tpl[0]
                    tail = tpl[1]
                head = head.next
            if hit:
                for i, j in hit_set:
                    board[i][j] = 'X'

    
    def getNbs(self, board: List[List[str]], loc: tuple, visited: set) -> tuple:
        head = None
        tail = None
        i = loc[0]
        j = loc[1]
        potnbs = [(i-1, j), (i, j-1), (i, j+1), (i+1, j)]
        for k, l in potnbs:
            if k >= 0 and k < len(board) and l < len(board[0]) and l >= 0 and board[k][l] == 'O' and board[k][l] not in visited:
                if head is None:
                    head = lnde((k, l))
                    tail = head
                else:
                    tail.next = lnde((k, l))
                    tail = tail.next
        return (head, tail)
            