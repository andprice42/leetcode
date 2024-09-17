# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        prev = None
        while ptr:
            if ptr.next and ptr.val == ptr.next.val:
                v = ptr.val
                while ptr and ptr.val == v:
                    ptr = ptr.next
                if prev:
                    prev.next = ptr
                else:
                    head = ptr
            else:
                prev = ptr
                ptr = ptr.next
        return head