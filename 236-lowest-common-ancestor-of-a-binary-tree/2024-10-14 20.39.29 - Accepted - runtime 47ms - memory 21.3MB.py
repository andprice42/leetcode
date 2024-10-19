# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        tpl = self.dfs(root, p.val, q.val)
        return tpl[0]
    def dfs(self, root: 'TreeNode', p: int, q: int) -> tuple:
        ltpl = None
        rtpl = None
        if root.left:
            ltpl = self.dfs(root.left, p, q)
        if ltpl and ltpl[1] and ltpl[2]:
            return ltpl
        if root.right:
            rtpl = self.dfs(root.right, p, q)
        if rtpl and rtpl[1] and rtpl[2]:
            return rtpl
        elif ltpl and rtpl and rtpl[1] and ltpl[2]:
            return (root, True, True)
        elif ltpl and rtpl and rtpl[2] and ltpl[1]:
            return (root, True, True)
        elif rtpl and ((root.val == p and rtpl[2]) or (root.val == q and rtpl[1])):
            return (root, True, True)
        elif ltpl and ((root.val == q and ltpl[1]) or (root.val == p and ltpl[2])):
            return (root, True, True)
        elif ltpl and rtpl:
            return (root, ltpl[1] or rtpl[1] or root.val == p, ltpl[2] or rtpl[2] or root.val == q)
        elif ltpl:
            return ltpl
        elif rtpl:
            return rtpl
        else:
            return (root, root.val == p, root.val == q)