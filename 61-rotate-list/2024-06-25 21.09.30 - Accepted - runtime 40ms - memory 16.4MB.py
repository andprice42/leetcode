# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        ln = 0
        ptr = head
        while ptr:
            prev = ptr
            ptr = ptr.next
            ln += 1
        if k >= ln:
            k = k % ln
        
        if k == 0:
            return head
        
        prev.next = head

        ptr = head
        ogln = ln
        while ln > k:
            ptr = ptr.next
            ln -= 1
        head = ptr

        while ogln > 1:
            ogln -= 1
            ptr = ptr.next
        ptr.next = None
        return head