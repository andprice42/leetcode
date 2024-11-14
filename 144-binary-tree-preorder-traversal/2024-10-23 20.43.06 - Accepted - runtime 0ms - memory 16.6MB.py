# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.dfs(root, [])

    def dfs(self, root: Optional[TreeNode], lst: List[int]) -> List[int]:
        if root is None:
            return []
        lst.append(root.val)
        if root.left:
            lst = self.dfs(root.left, lst)
        if root.right:
            lst = self.dfs(root.right, lst)
        return lst