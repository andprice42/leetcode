# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        lrt = root.left
        rrt = root.right
        return self.recurse(lrt, rrt)
    
    def recurse(self, lrt, rrt):
        if lrt is None and rrt is None:
            return True
        elif lrt is None or rrt is None:
            return False
        elif lrt.val != rrt.val:
            return False
        else:
            val = self.recurse(lrt.left, rrt.right)
            if val:
                val = self.recurse(lrt.right, rrt.left)
        return val