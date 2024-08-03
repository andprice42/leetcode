
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
import queue
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        visited = {}
        new_node = Node(node.val, [neb.val for neb in node.neighbors])
        visited[new_node.val] = new_node
        fq = queue.Queue()
        [fq.put(nb) for nb in node.neighbors if visited.get(nb.val) is None]
        while (fq.empty() is False):
            nb = fq.get()
            nnb = Node(nb.val, [neb.val for neb in nb.neighbors])
            visited[nnb.val] = nnb
            [fq.put(nbn) for nbn in nb.neighbors if visited.get(nbn.val) is None]
        
        for ky in visited.keys():
            nd = visited[ky]
            nd.neighbors = [visited[ky1] for ky1 in nd.neighbors]
        
        return new_node


            




        