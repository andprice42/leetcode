# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mp = {}
        ptr = head
        i = 0
        while ptr:
            mp[ptr] = i
            ptr = ptr.next
            i += 1

        nmp = {}
        nhead = None
        ptr = None
        i = 0
        while head:
            if nmp.get(i) is None:
                nnde = Node(head.val)
                nmp[i] = nnde
            else:
                nnde = nmp.get(i)
            ic = mp.get(head.random)
            if head.random and nmp.get(ic) is None:
                nrndm = Node(head.random.val)
                nmp[ic] = nrndm
            elif head.random is None:
                nrndm = None
            else:
                nrndm = nmp.get(ic)
            nnde.random = nrndm
            if nhead is None:
                nhead = nnde
                prev = nnde
            else:
                prev.next = nnde
                prev = nnde
            
            i += 1
            head = head.next
        # while nhead:
        #     print(nhead.val)
        #     print(nhead.random)
        #     nhead = nhead.next
        return nhead