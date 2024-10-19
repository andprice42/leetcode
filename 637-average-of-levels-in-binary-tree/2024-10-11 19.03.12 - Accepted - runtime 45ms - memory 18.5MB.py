# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        nodes = [root]
        avgs = []
        i = 0
        while len(nodes) > 0:
            nndes = []
            avg = [0, 0]
            for nde in nodes:
                avg[0] += 1
                avg[1] += nde.val
                if nde.left:
                    nndes.append(nde.left)
                if nde.right:
                    nndes.append(nde.right)
            avgs.append(avg[1]/avg[0])
            nodes = nndes
        return avgs