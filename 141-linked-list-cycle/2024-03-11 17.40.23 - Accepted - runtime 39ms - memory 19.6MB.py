# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        prevNodes = set()
        node = head
        while (node.next):
            if node in prevNodes:
                return True
            prevNodes.add(node)
            node = node.next
            if node is None:
                return False
        return False
        