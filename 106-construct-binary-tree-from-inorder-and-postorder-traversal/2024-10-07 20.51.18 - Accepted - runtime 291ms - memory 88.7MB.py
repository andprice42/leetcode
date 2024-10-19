# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        tpl = self.recurse(inorder, postorder)
        if tpl:
            return tpl[1]
        else:
            return None
    def recurse(self, inorder: List[int], postorder: List[int]) -> tuple:
        if len(inorder) == 0 or len(postorder) == 0:
            return None
        root = TreeNode(postorder[-1])
        for i in range(len(inorder)):
            if inorder[i] == root.val:
                break
            i += 1
        left_tree = inorder[:i]
        right_tree = inorder[i+1:]
        postorder = postorder[:-1]
        rtpl = self.recurse(right_tree, postorder)
        if rtpl:
            postorder = rtpl[0]
            root.right = rtpl[1]
        ltpl = self.recurse(left_tree, postorder)
        if ltpl:
            postorder = ltpl[0]
            root.left = ltpl[1]
        return (postorder, root)
