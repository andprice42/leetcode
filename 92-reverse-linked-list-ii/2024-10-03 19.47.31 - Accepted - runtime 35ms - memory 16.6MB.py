# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        ptr = head
        prev = None
        reverse = False
        i = 1
        while ptr:
            if i == left:
                start = prev
                end = ptr
                prev = ptr
                ptr = ptr.next
                reverse = True

            elif i == right:
                end.next = ptr.next
                ptr.next = prev
                if start:
                    start.next = ptr
                else:
                    head = ptr
                return head
            
            elif reverse:
                nptr = ptr.next
                ptr.next = prev
                prev = ptr
                ptr = nptr

            else:
                prev = ptr
                ptr = ptr.next
            i += 1
        return head

        