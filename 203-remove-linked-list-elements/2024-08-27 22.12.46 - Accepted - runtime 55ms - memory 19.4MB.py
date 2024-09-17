# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
        prev = head
        if head:
            ptr = head.next
            while ptr:
                if ptr.val == val:
                    prev.next = ptr.next
                else:
                    prev = ptr
                ptr = ptr.next
        return head
