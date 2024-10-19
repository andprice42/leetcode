# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        tpl = self.dfs(root)
        return tpl[0]
    
    def dfs(self, root: Optional[TreeNode]) -> tuple:
        ltpl = None
        rtpl = None
        if root.left:
            ltpl = self.dfs(root.left)
        if root.right:
            rtpl = self.dfs(root.right)
        if ltpl and rtpl:
            return (min(ltpl[0], rtpl[0], abs(root.val-ltpl[2]), abs(root.val-rtpl[1])), ltpl[1], rtpl[2])
        elif ltpl:
            return (min(ltpl[0], abs(root.val-ltpl[2])), ltpl[1], root.val)
        elif rtpl:
            return (min(rtpl[0], abs(root.val-rtpl[1])), root.val, rtpl[2])
        else:
            return (1000000000, root.val, root.val)

        
