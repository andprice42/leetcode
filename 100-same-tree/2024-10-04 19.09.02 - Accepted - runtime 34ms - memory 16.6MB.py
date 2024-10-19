# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.dfs(p, q)
    def dfs(self,  p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is None and q:
            return False
        elif p and q is None:
            return False
        elif p.val != q.val:
            return False
        rt = self.dfs(p.right, q.right)
        lt = self.dfs(p.left, q.left)
        if rt and lt:
            return True
        else:
            return False
        