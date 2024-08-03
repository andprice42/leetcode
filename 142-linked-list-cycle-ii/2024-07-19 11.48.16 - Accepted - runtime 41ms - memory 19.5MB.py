# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        st = set()
        ptr = head
        while ptr:
            if ptr in st:
                return ptr
            else:
                st.add(ptr)
            ptr = ptr.next
        return None
