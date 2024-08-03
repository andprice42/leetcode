# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cptr = head
        ln = 0
        while cptr:
            cptr = cptr.next
            ln += 1
        if ln == 1 and n == 1:
            return None
        prev = head
        cptr = head
        while ln > n and cptr.next:
            prev = cptr
            cptr = cptr.next
            ln -= 1
        if cptr == head:
            return cptr.next
        prev.next = cptr.next
        
        return head
        