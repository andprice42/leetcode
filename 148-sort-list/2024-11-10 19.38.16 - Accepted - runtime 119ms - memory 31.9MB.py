# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        ln = 0
        while ptr:
            ptr = ptr.next
            ln += 1
        nhead, ntail = self.recurse(head, ln)
        return nhead

    def recurse(self, head: Optional[ListNode], ln: int) -> tuple:
        if head is None or head.next is None:
            return (head, head)
        lhead = head
        med = ln // 2
        cnt = 0
        rhead = head
        while cnt < med:
            prev = rhead
            rhead = rhead.next
            cnt += 1
        prev.next = None
        lhead, ltail = self.recurse(lhead, med)
        rhead, rtail = self.recurse(rhead, ln-med)
        if lhead is None and rhead:
            return (rhead, rhead)
        elif rhead is None and lhead:
            return (lhead, lhead)
        elif rtail.val <= lhead.val:
            rtail.next = lhead
            return (rhead, ltail)
        elif ltail.val <= rhead.val:
            ltail.next = rhead
            return (lhead, rtail)
        if lhead.val <= rhead.val:
            head = lhead
        else:
            head = rhead
        lptr = lhead
        rptr = rhead
        while lptr and rptr:
            lprev = None
            while lptr and rptr.val >= lptr.val:
                lprev = lptr
                lptr = lptr.next
            if lprev:
                lprev.next = rptr
                tail = rtail
            else:
                tail = ltail
            rprev = None
            while rptr and lptr and lptr.val >= rptr.val:
                rprev = rptr
                rptr = rptr.next
            if lptr:
                rprev.next = lptr
                tail = ltail
        return (head, tail)
