# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = None
        if root.left:
            llst = self.binaryTreePaths(root.left)
            paths = [str(root.val) + "->" + i for i in llst]
        if root.right:
            rlst = self.binaryTreePaths(root.right)
            if paths:
                [paths.append(str(root.val) + "->" + i) for i in rlst]
            else:
                paths = [str(root.val) + "->" + i for i in rlst]
        if paths is None:
            paths = [str(root.val)]
        return paths

        