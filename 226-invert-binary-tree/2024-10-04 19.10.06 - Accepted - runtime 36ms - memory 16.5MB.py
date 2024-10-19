# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None or root == []:
            return root
        left = root.left
        right = root.right
        root.left = right
        root.right = left
        sol = Solution()
        if (root.left):
            root.left = sol.invertTree(root.left)
        if (root.right):
            root.right = sol.invertTree(root.right)
        return root