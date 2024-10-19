# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class lifoQ:
    def __init__(self, val: Optional[TreeNode], nxt=None):
        self.val = val
        self.next = nxt

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        ret_arr = [[root.val]]
        tail = lifoQ(TreeNode(101))
        if root.left:
            nnde = lifoQ(root.left)
            nnde.next = tail
            if root.right:
                head = lifoQ(root.right)
                head.next = nnde
            else:
                head = nnde
        elif root.right:
            head = lifoQ(root.right)
            head.next = tail
        else:
            return ret_arr
        left = False
        while head:
            new_arr = []
            if left:
                left = False
            else:
                left = True
            atail = None
            while head.val.val != 101:
                new_arr.append(head.val.val)
                if left and head.val.right:
                    nnde = lifoQ(head.val.right)
                    if tail.next:
                        nnde.next = tail.next
                    else:
                        atail = nnde
                    tail.next = nnde
                if left and head.val.left:
                    nnde = lifoQ(head.val.left)
                    if tail.next:
                        nnde.next = tail.next
                    else:
                        atail = nnde
                    tail.next = nnde
                if left is False and head.val.left:
                    nnde = lifoQ(head.val.left)
                    if tail.next:
                        nnde.next = tail.next
                    else:
                        atail = nnde
                    tail.next = nnde
                if left is False and head.val.right:
                    nnde = lifoQ(head.val.right)
                    if tail.next:
                        nnde.next = tail.next
                    else:
                        atail = nnde
                    tail.next = nnde
                head = head.next

            ret_arr.append(new_arr)
            head = head.next
            tail = atail
            if tail:
                tail.next = lifoQ(TreeNode(101))
                tail = tail.next
        return ret_arr

