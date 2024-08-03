# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        arr = []
        nde = head
        while nde:
            arr.append(nde.val)
            nde = nde.next
        return self.recurse(arr)
    
    def recurse(self, arr: List[int]) -> Optional[TreeNode]:
        if len(arr) == 0:
            return None
        ln = len(arr)
        med = ln // 2
        la = arr[:med]
        ra = arr[med+1:]
        ln = self.recurse(la)
        rn = self.recurse(ra)
        tnde = TreeNode(arr[med], ln, rn)
        return tnde