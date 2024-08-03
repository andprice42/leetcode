# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        return self.recurse(root, 0, targetSum)

    def recurse(self, root, sm, targetSum) -> bool:
        ret_val = False
        if root.left is None and root.right is None:
            return (sm + root.val) == targetSum
        if root.left:
            ret_val = self.recurse(root.left, sm + root.val, targetSum)
        if ret_val:
            return ret_val
        if root.right:
            ret_val = self.recurse(root.right, sm + root.val, targetSum)
        if ret_val:
            return ret_val
        return ret_val

        