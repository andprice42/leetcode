# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        prev = None
        oghd = head
        while head and head.next:
            if prev is None:
                prev = head
            elif head.val == prev.val:
                prev.next = head.next
            else:
                prev = head
            head = head.next
        if head and head.val == prev.val:
            prev.next = None
        return oghd

        