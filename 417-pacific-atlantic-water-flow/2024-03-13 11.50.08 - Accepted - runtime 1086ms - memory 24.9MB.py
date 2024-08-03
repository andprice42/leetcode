class Node:
    def __init__(self, row: int, col: int, elev: int):
        self.row = row
        self.col = col
        self.elev = elev
        self.neighbors = []
import queue
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        graph = {}
        visited = {}
        if heights is None:
            return None
        elif heights == []:
            return None
        rows = len(heights)
        cols = len(heights[0])
        for i in range(rows):
            for j in range(cols):
                cht = heights[i][j]
                if graph.get((i, j)) is None:
                    nd = Node(i, j, cht)
                    graph[(i, j)] = nd
                else:
                    nd = graph[(i,j)]

                if i + 1 < rows:
                    dht = heights[i+1][j]
                    if graph.get((i+1, j)) is None:
                        nbnd = Node(i+1, j, dht)
                        graph[(i+1, j)] = nbnd
                    else:
                        nbnd = graph[(i+1,j)]
                    if dht <= cht:
                        nd.neighbors.append(nbnd)

                if i - 1 >= 0:
                    uht = heights[i-1][j]
                    if graph.get((i-1, j)) is None:
                        nbnd = Node(i-1, j, uht)
                        graph[(i-1, j)] = nbnd
                    else:
                        nbnd = graph[(i-1,j)]
                    if uht <= cht:
                        nd.neighbors.append(nbnd)
                
                if j + 1 < cols:
                    rht = heights[i][j+1]
                    if graph.get((i, j+1)) is None:
                        nbnd = Node(i, j+1, rht)
                        graph[(i, j+1)] = nbnd
                    else:
                        nbnd = graph[(i,j+1)]
                    if rht <= cht:
                        nd.neighbors.append(nbnd)
                
                if j - 1 >= 0:
                    lht = heights[i][j-1]
                    if graph.get((i, j-1)) is None:
                        nbnd = Node(i, j-1, lht)
                        graph[(i, j-1)] = nbnd
                    else:
                        nbnd = graph[(i,j-1)]
                    if lht <= cht:
                        nd.neighbors.append(nbnd)
                
                if i+1 == rows or j+1 == cols:
                    atl = Node(i+1, j+1, -1)
                    nd.neighbors.append(atl)
                if i-1 == -1 or j-1 == -1:
                    pac = Node(i-1, j-1, -2)
                    nd.neighbors.append(pac)
        sol = Solution()
        both = set()
        pq = queue.PriorityQueue()
        for i in range(rows):
            for j in range(cols):
                nde = graph[(i, j)]
                pq.put((nde.elev, (i, j)))
        cnt = 0
        while pq.empty() is False and cnt < 2:
            qit = pq.get()
            i = qit[1][0]
            j = qit[1][1]
            snde = graph[(i, j)]
            visited = sol.dfs(visited, graph, snde)
            if visited.get((i, j)) and visited.get((i, j)) == [True, True]:
                both.add((i, j))
            
        print(len(visited))
        print(rows*cols)
        both_list = [item for item in both]
        return both_list

    def dfs(self, visited, graph, nde):
        if nde.elev == -1:
            visited[(nde.row-1, nde.col-1)][0] = True
            return visited
        elif nde.elev == -2:
            visited[(nde.row+1, nde.col+1)][1] = True
            return visited

        visited[(nde.row, nde.col)] = [False, False]

        sol = Solution()
        for nb in nde.neighbors:
            if visited.get((nb.row, nb.col)) is None:
                visited = sol.dfs(visited, graph, nb)
            elif visited.get((nb.row, nb.col)):
                if visited[(nb.row, nb.col)][0] == True:
                    visited[(nde.row, nde.col)][0] = True
                if visited[(nb.row, nb.col)][1] == True:
                    visited[(nde.row, nde.col)][1] = True
        for nb in nde.neighbors:
            if nde in nb.neighbors:
                if visited[(nde.row, nde.col)][0] == True:
                    visited[(nb.row, nb.col)][0] = True
                if visited[(nde.row, nde.col)][1] == True:
                    visited[(nb.row, nb.col)][1] = True
        return visited
