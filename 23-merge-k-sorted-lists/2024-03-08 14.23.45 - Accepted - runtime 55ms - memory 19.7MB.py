# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if (len(lists) == 0):
            return None
        heap = []
        for node in lists:
            if node is None:
                continue
            nd = node
            while (nd.next):
                heapq.heappush(heap, nd.val)
                nd = nd.next
                prev = nd
            heapq.heappush(heap, nd.val)
            
        head = None
        if (heap):
            head = ListNode(heapq.heappop(heap), None)
            prev = head
            while (len(heap) > 0):
                node = ListNode(heapq.heappop(heap), None)
                prev.next = node
                prev = node
                node.next = None
        return head

        