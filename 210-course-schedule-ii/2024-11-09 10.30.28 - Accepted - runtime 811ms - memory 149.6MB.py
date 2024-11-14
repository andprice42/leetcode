class Node:
    def __init__(self, val: int):
        self.val = val
        self.fq = []

class lnde:
    def __init__(self, val: List[Optional['Node']], next: Optional['lnde'] = None):
        self.val = val
        self.next = next

class Solution:
    def findCycle(self, ohead: Optional['Node'], visited: set) -> bool:
        lst = ohead.fq
        visited_copy = set([i for i in visited])
        for item in lst:
            if item.val in visited_copy:
                return True
            visited_copy.add(item.val)
            bln = self.findCycle(item, visited_copy)
            visited_copy.remove(item.val)
            if bln:
                return True
        return False

    def bfs(self, head: Optional['Node']) -> List[int]:
        ret_arr = [head.val]
        fq = lnde([head])
        fq.next = lnde(head.fq)
        tail = fq.next
        while fq:
            for nde in fq.val:
                if nde.val in ret_arr:
                    ret_arr = [v for v in ret_arr if v != nde.val]
                ret_arr.append(nde.val)
                tail.next = lnde(nde.fq)
                tail = tail.next
            fq = fq.next
        return ret_arr

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        roots = set()
        pairs = set()
        deps = set()
        nmap = {}
        for r, p in prerequisites:
            if (p, r) in pairs:
                return []
            else:
                pairs.add((r, p))
            if nmap.get(p) is None:
                pnde = Node(p)
                nmap[p] = pnde
            if nmap.get(r) is None:
                rnde = Node(r)
                nmap[r] = rnde
            else:
                rnde = nmap[r]
            nmap[p].fq.append(rnde)

            if p not in deps:
                roots.add(p)
            deps.add(r)
            if r in roots:
                roots.remove(r)
                roots.add(p)
        fin_arr = [i for i in roots]
        for i in roots:
            if self.findCycle(nmap[i], set([i])):
                return []
            ret_arr = self.bfs(nmap[i])
            fin_arr = [i for i in fin_arr if i not in ret_arr]
            [fin_arr.append(j) for j in ret_arr]

        if len(fin_arr) != numCourses:
            [fin_arr.append(i) for i in range(numCourses) if i not in fin_arr]
        elif len(roots) == 0:
            return []
        return fin_arr 