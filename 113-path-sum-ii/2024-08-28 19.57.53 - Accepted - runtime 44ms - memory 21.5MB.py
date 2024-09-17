# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        return self.dfs(root, targetSum, root.val, [root.val])
    def dfs(self, node: Optional[TreeNode], targetSum: int, sm: int, path: List[int]) -> List[List[int]]:
        if sm == targetSum and node.left is None and node.right is None:
            return [path]
        path_cpy = [i for i in path]
        ret_paths = []
        if node.left:
            path_cpy.append(node.left.val)
            lpaths = self.dfs(node.left, targetSum, sm + node.left.val, path_cpy)
            ret_paths = [i for i in lpaths]
            path_cpy = path_cpy[:-1]
        if node.right:
            path_cpy.append(node.right.val)
            rpaths = self.dfs(node.right, targetSum, sm + node.right.val, path_cpy)
            [ret_paths.append(j) for j in rpaths]
            path_cpy = path_cpy[:-1]
        return ret_paths