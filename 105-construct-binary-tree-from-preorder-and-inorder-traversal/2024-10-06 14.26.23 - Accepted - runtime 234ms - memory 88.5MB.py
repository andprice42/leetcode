# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        tpl = self.recurse(preorder, inorder)
        if tpl:
            return tpl[2]
        else:
            return None
    def recurse(self, preorder: List[int], inorder: List[int]) -> tuple:
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        root = TreeNode(preorder[0])
        i = 0
        for n in inorder:
            if n == root.val:
                break
            i += 1
        left_tree = inorder[:i]
        right_tree = inorder[i+1:]
        preorder = preorder[1:]
        ltpl = self.recurse(preorder, left_tree)
        if ltpl:
            preorder = ltpl[0]
            inorder = ltpl[1]
            root.left = ltpl[2]
        rtpl = self.recurse(preorder, right_tree)
        if rtpl:
            preorder = rtpl[0]
            inorder = rtpl[1]
            root.right = rtpl[2]
        return (preorder, inorder, root)