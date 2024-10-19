# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        tail = self.dfs(root)
    def dfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ltail = None
        rtail = None
        if root is None:
            return None
        if root.left:
            ltail = self.dfs(root.left)
        if root.right:
            rtail = self.dfs(root.right)
        if ltail and rtail:
            ltail.right = root.right
            root.right = root.left
            root.left = None
            return rtail
        elif ltail:
            root.right = root.left
            root.left = None
            return ltail
        elif rtail:
            return rtail
        else:
            return root
        