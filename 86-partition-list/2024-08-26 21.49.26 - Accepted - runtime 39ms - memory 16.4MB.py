# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        ptr = head
        prev = None
        target_exceeded = False
        while ptr:
            if ptr.val >= x:
                target_exceeded = True
                prev = ptr
            elif ptr.val < x and prev and target_exceeded:
                nptr = ListNode(ptr.val)
                nhead = head
                nprev = None
                cnt = 0
                while nhead and nhead.val < x:
                    nprev = nhead
                    nhead = nhead.next
                if nhead:
                    prev.next = ptr.next
                    if nprev:
                        nprev.next = nptr
                    else:
                        head = nptr
                    nptr.next = nhead
            else:
                prev = ptr
            ptr = ptr.next
        return head
            
                