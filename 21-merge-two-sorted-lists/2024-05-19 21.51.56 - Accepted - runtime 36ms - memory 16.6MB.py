# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = list1
        h2 = list2
        n1 = h1
        n2 = h2
        if h1 is None and h2 is None:
            return None
        elif h1 is None:
            return h2
        elif h2 is None:
            return h1
        elif h1.val > h2.val:
            h3 = ListNode(h2.val)
            node = h3
            prev = h3
            n2 = n2.next
        else:
            h3 = ListNode(h1.val)
            node = h3
            prev = h3
            n1 = n1.next

        while n1 and n2:
            if n1.val > n2.val:
                node = ListNode(n2.val)
                prev.next = node
                prev = node
                n2 = n2.next
            else:
                node = ListNode(n1.val)
                prev.next = node
                prev = node
                n1 = n1.next
            
        if n1:
            while n1:
                node = ListNode(n1.val)
                prev.next = node
                prev = node
                n1 = n1.next
        elif n2:
            while n2:
                node = ListNode(n2.val)
                prev.next = node
                prev = node
                n2 = n2.next
        return h3
        
            
    

        