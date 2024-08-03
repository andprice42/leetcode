# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        if root is None:
            return lst
        if root.left:
            lst = self.inorderTraversal(root.left)
        
        lst.append(root.val)
        if root.right:
            lst2 = self.inorderTraversal(root.right)
            [lst.append(val) for val in lst2]
        return lst
            