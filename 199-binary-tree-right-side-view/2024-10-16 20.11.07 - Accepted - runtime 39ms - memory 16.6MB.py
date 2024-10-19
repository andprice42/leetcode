# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class lnde:
    def __init__(self, val: Optional[TreeNode], next: Optional['lnde'] = None):
        self.val = val
        self.next = next

class Solution: 
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        q = lnde(root)
        ret_lst = []
        while q:
            hq = None
            tq = None
            first = True
            while q:
                if first:
                    ret_lst.append(q.val.val)
                    first = False
                if q.val.right:
                    if hq is None:
                        hq = lnde(q.val.right)
                        tq = hq
                    else:
                        tq.next = lnde(q.val.right)
                        tq = tq.next
                if q.val.left:
                    if hq is None:
                        hq = lnde(q.val.left)
                        tq = hq
                    else:
                        tq.next = lnde(q.val.left)
                        tq = tq.next
                prev = q
                q = q.next
            q = hq
        return ret_lst
