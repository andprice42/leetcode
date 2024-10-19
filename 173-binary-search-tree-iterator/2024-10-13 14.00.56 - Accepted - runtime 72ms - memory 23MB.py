# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class lnde:
    def __init__(self, val: int, nxt):
        self.val = val
        self.next = nxt

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.head = self.dfs(root)[0]

    def next(self) -> int:
        # print(self.head.val)
        v = self.head.val
        self.head = self.head.next
        return v

    def hasNext(self) -> bool:
        if self.head:
            return True
        else:
            return False
    def dfs(self, root: Optional[TreeNode]) -> tuple:
        ltpl = None
        rtpl = None
        if root.left:
            tpl = self.dfs(root.left)
            ltpl = tpl
        if root.right:
            rtpl = self.dfs(root.right)

        if ltpl and rtpl:
            lhead = ltpl[0]
            ltail = ltpl[1]
            rhead = rtpl[0]
            rtail = rtpl[1]
            ltail.next = lnde(root.val, rhead)
            return (lhead, rtail)
        elif ltpl:
            lhead = ltpl[0]
            ltail = ltpl[1]
            ltail.next = lnde(root.val, None)
            tail = ltail.next
            return (lhead, tail)
        elif rtpl:
            rhead = rtpl[0]
            rtail = rtpl[1]
            head = lnde(root.val, rhead)
            return (head, rtail)
        else:
            nhead = lnde(root.val, None)
            return (nhead, nhead)
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()