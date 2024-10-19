# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        tpl = self.dfs(root)
        return tpl[0]
    def dfs(self, root: Optional[TreeNode]) -> tuple:
        if root.left is None and root.right is None:
            return (root.val, root.val)
        mx = None
        curr = None
        if root.left:
            ltpl = self.dfs(root.left)
            mx = max(ltpl[0], ltpl[1] + root.val, root.val)
            curr = max(ltpl[1] + root.val, root.val)
        if root.right:
            rtpl = self.dfs(root.right)
            if mx:
                mx = max(mx, rtpl[0], rtpl[1] + root.val, rtpl[1] + root.val + ltpl[1])
            else:
                mx = max(rtpl[0], rtpl[1] + root.val, root.val)
            if curr:
                curr = max(curr, rtpl[1] + root.val)
            else:
                curr = max(root.val, rtpl[1] + root.val)
        return (mx, curr)