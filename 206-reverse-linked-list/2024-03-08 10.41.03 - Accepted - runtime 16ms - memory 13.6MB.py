# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        node = head
        prev = head
        node = node.next
        prev.next = None
        if node is None:
            return prev
        if node.next is None:
            node.next = prev
            return node
        while (node.next):
            curr = node
            node = node.next
            curr.next = prev
            prev = curr
            if node.next is None:
                node.next = prev
                return node

        return node





        