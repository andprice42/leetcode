# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        elif (root.left is None and root.right is None):
            return 1
        mnl = -1
        mnr = -1
        if root.left:
            mnl = self.minDepth(root.left) + 1
        if root.right:
            mnr = self.minDepth(root.right) + 1
        if mnl > 0 and mnr > 0:
            return min(mnl, mnr)
        elif mnl < 0:
            return mnr
        else:
            return mnl