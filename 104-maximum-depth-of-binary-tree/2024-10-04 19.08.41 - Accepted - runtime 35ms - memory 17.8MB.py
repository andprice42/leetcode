# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if (root is None):
            return 0
            
        if (root.left or root.right):
            arr = [root.left, root.right]
            childs = []
            for e in arr:
                if e:
                    childs.append(e)
            dmax = 0
            for c in childs:
                sol = Solution()
                d = sol.maxDepth(c)
                if d > dmax:
                    dmax = d
        else:
            dmax = 0
        dmax += 1
        return dmax