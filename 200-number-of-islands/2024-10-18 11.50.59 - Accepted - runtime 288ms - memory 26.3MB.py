class lnde:
    def __init__(self, val: tuple, next: Optional['lnde'] = None):
        self.val = val
        self.next = next
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        cnt = 0
        visit = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    visit.add((i, j))
        while len(visit) > 0:
            cnt += 1
            i, j = visit.pop()
            visited.add((i, j))
            tpl = self.getNeighbors(grid, (i, j), visited)
            head = tpl[0]
            tail = tpl[1]
            while head:
                if head.val in visited:
                    head = head.next
                    continue
                visited.add(head.val)
                visit.remove(head.val)
                tpl = self.getNeighbors(grid, head.val, visited)
                tail.next = tpl[0]
                if tpl[1]:
                    tail = tpl[1]
                head = head.next
        return cnt

    def getNeighbors(self, grid: List[List[str]], loc: tuple, visited: set) -> tuple:
        i = loc[0]
        j = loc[1]
        potnbs = [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]
        head = None
        tail = None
        for k, l in potnbs:
            if k >= 0 and k < len(grid) and l >= 0 and l < len(grid[0]) and (k, l) not in visited and grid[k][l] == "1":
                if head is None:
                    head = lnde((k, l))
                    tail = head
                else:
                    tail.next = lnde((k, l))
                    tail = tail.next
        return (head, tail)