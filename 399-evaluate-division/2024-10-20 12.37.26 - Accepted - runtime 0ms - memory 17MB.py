class lnde:
    def __init__(self, val: tuple, next: tuple = None):
        self.val = val
        self.next = next

class Graph:
    def __init__(self, val: str):
        self.val = val
        self.head = None
        self.tail = None

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        ptr_map = {}
        for i in range(len(values)):
            eq = equations[i]
            if ptr_map.get(eq[1]) is None:
                ptr_map[eq[1]] = Graph(eq[1])
            
            if ptr_map.get(eq[0]) is None:
                ptr_map[eq[0]] = Graph(eq[0])
            nnde = lnde((values[i], ptr_map[eq[0]]))
            nnde1 = lnde((1/values[i], ptr_map[eq[1]]))
            if ptr_map[eq[1]].head:
                ptr_map[eq[1]].tail.next = nnde
            else:
                ptr_map[eq[1]].head = nnde
            ptr_map[eq[1]].tail = nnde

            if ptr_map[eq[0]].head:
                ptr_map[eq[0]].tail.next = nnde1
            else:
                ptr_map[eq[0]].head = nnde1        
            ptr_map[eq[0]].tail = nnde1

        rvs = []
        for query in queries:
            head = ptr_map.get(query[1])
            tail = ptr_map.get(query[0])
            if head is None or tail is None:
                rvs.append(-1.00)
            else:
                v = self.dfs(head, tail, 1.0, set())
                rvs.append(v)
        return rvs

    def dfs(self, head: Optional['Graph'], tail: Optional['Graph'], factor: float, visited: set) -> float:
        if head == tail:
            return factor
        visited.add(head.val)
        ptr = head.head
        while ptr:
            if ptr.val[1].val not in visited:
                v = self.dfs(ptr.val[1], tail, factor*ptr.val[0], visited)
                if v != -1.0:
                    return v
            ptr = ptr.next
        return -1.0



