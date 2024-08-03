# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        ptr = head
        nhd = ListNode(head.next.val)
        prev = ListNode(head.val)
        nhd.next = prev
        ptr = ptr.next.next
        if ptr and ptr.next is None:
            prev.next = ptr
            return nhd
        while ptr and ptr.next:
            pos2 = ListNode(ptr.val)
            pos1 = ListNode(ptr.next.val)
            prev.next = pos1
            pos1.next = pos2
            prev = pos2
            ptr = ptr.next.next
        if ptr:
            pos2.next = ptr
        return nhd