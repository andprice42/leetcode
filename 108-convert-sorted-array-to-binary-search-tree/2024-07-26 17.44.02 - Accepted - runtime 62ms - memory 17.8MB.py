# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        ln = len(nums)
        med = ln // 2
        nde = TreeNode(nums[med])
        nl = nums[:med]
        nr = nums[med+1:]
        nde.left = self.sortedArrayToBST(nl)
        nde.right = self.sortedArrayToBST(nr)
        return nde