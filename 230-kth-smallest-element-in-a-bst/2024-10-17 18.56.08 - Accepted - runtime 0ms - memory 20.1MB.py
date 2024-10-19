# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        tpl = self.dfs(root, k, 0)
        return tpl[0]
    def dfs(self, root: Optional[TreeNode], k: int, v: int) -> tuple:
        ltpl = None
        rtpl = None
        if root.left:
            ltpl = self.dfs(root.left, k, v)
            if ltpl[0] is not None:
                return ltpl
        if ltpl:
            v = ltpl[1] + 1
        else:
            v += 1
    
        if k-v == 0:
            return (root.val, v)

        if root.right:
            rtpl = self.dfs(root.right, k, v)
            return rtpl
        elif ltpl:
            return (None, v)
        else:
            return (None, v)