# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.recurse(root, 0, "")

    def recurse(self, root: Optional[TreeNode], sm: int, s: str) -> int:
        if root.left is None and root.right is None:
            sm += int(s + str(root.val))
            return sm
        if root.left:
            sm = self.recurse(root.left, sm, s + str(root.val))
        if root.right:
            sm = self.recurse(root.right, sm, s + str(root.val))
        return sm