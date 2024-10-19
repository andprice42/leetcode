# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        bln, mn_val = self.helper(root, None)
        return bln

    def helper(self, root: Optional[TreeNode], mn_val: int) -> tuple:
        if root is None:
            return (True, mn_val)
        elif mn_val and root.val < mn_val:
            return (False, mn_val)
        if root.left and root.left.val >= root.val:
            return (False, mn_val)
        elif root.right and root.right.val <= root.val:
            return (False, mn_val)

        bln, mn_val = self.helper(root.left, mn_val)
        if mn_val and mn_val >= root.val:
            return (False, mn_val)         
        mn_val = root.val
        if bln is False:
            return (bln, mn_val)
        return self.helper(root.right, mn_val)