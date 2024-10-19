# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        i = 1
        ptr = head
        prev = head
        ktl = head
        lnd = None
        while i < k and ptr.next: 
            ptr = ptr.next
            lnd = ListNode(ptr.val, prev)
            prev = lnd
            i += 1
        if i < k or k == 1:
            return head
        else:
            head = lnd

        while True:
            ktlprev = ktl
            ktl = ptr.next
            prev = ptr.next
            ptr = ptr.next
            lnd = None
            i = 1
            while i < k and ptr and ptr.next:
                ptr = ptr.next
                lnd = ListNode(ptr.val, prev)
                prev = lnd
                i += 1
            if ktl is None or ktl.next is None:
                ktlprev.next = ptr
                return head
            elif i < k:
                ktlprev.next = ktl
                return head
            else:
                ktlprev.next = lnd