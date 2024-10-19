# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = l1
        val_arr = [node.val]
        ln = 1
        while node.next:
            node = node.next
            val_arr.append(node.val)
            ln += 1
        fin_val_arr = [str(val_arr[i]) for i in range(ln-1, -1, -1)]
        num1 = int(''.join(fin_val_arr))
        node = l2
        val_arr = [node.val]
        ln = 1
        while node.next:
            node = node.next
            val_arr.append(node.val)
            ln += 1
        fin_val_arr = [str(val_arr[i]) for i in range(ln-1, -1, -1)]
        num2 = int(''.join(fin_val_arr))
        num3str = str(num1 + num2)
        tail = True
        for i in range(len(num3str)):
            if tail:
                node = ListNode(num3str[i])
                tail = False
            else:
                node = ListNode(num3str[i], prevnode)
            prevnode = node
        return node