class Node:
    def __init__(self, data: int):
        self.data = data
        self.neighbors = []
        self.parents = set()

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if (len(prerequisites) == 0):
            return True
        nodemap = {}
        for pr in prerequisites:
            c = pr[0]
            p = pr[1]
            if c == p:
                return False
            if nodemap.get(c) is None:
                nd = Node(c)
                if (nodemap.get(p) is None):
                    nb = Node(p)
                    nodemap[p] = nb
                else:
                    nb = nodemap[p]

                nd.neighbors.append(nb)
                nodemap[c] = nd
            else:
                nd = nodemap.get(c)
                if (nodemap.get(p) is None):
                    nb = Node(p)
                    nodemap[p] = nb
                else:
                    nb = nodemap[p]
                nd.neighbors.append(nb)
            nb.parents.add(c)
            [nb.parents.add(prnt) for prnt in nd.parents]
        sol = Solution()
        visited = {}
        for k, v in nodemap.items():
            visited[k] = False
        for i in range(0, numCourses):
            nd = nodemap.get(i)
            if (nd):
                ret_val = sol.dfs(nd, visited)
                if ret_val is False:
                    return False
        return True
    
    def dfs(self, nde: Node, visited: [int, bool]) -> bool:
        sol = Solution()
        ret_val = True
        visited[nde.data] = True
        if len(nde.neighbors) == 0:
            return True
        for nb in nde.neighbors:
            nb_data = [nb1.data for nb1 in nb.neighbors]
            if nde.data in nb_data:
                return False
            for prt in nde.parents:
                if prt in nb_data:
                    return False
                elif prt == nb.data:
                    return False
            if visited[nb.data] is False:
                ret_val = sol.dfs(nb, visited)
            if ret_val is False:
                return False
        return ret_val






    
        