# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class lnde:
    def __init__(self, val: Optional['Node'], nxt: Optional['lnde'] = None):
        self.val = val
        self.next = nxt

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        head = lnde(root)
        tail = head
        while head:
            nhead = None
            ntail = None
            while head:
                if head.val.left:
                    if nhead is None:
                        nhead = lnde(head.val.left)
                        ntail = nhead
                    else:
                        ntail.next = lnde(head.val.left)
                        ntail = ntail.next

                if head.val.right:
                    if nhead is None:
                        nhead = lnde(head.val.right)
                        ntail = nhead
                    else:
                        ntail.next = lnde(head.val.right)
                        ntail = ntail.next
                if head.next:
                    head.val.next = head.next.val
                head = head.next
            head = nhead
        return root

