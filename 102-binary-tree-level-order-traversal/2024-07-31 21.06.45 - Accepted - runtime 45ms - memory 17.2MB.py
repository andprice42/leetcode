# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class fifoQ:
    def __init__(self, node=None, next=None):
        self.node = node
        self.next = next

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        vals = []
        if root:
            vals.append([root.val])
        else:
            return vals
        head = None
        if root.left:
            head = fifoQ(root.left)
        elif root.right:
            head = fifoQ(root.right)
        
        if root.right and root.left:
            tail = fifoQ(root.right)
            head.next = tail
        else:
            tail = head
        otl = tail
        children = []
        while head:
            if head.node.left:
                tail.next = fifoQ(head.node.left)
                tail = tail.next
            if head.node.right:
                tail.next = fifoQ(head.node.right)
                tail = tail.next

            children.append(head.node.val)
            if otl == head:
                vals.append(children)
                children = []
                otl = tail
            head = head.next
        return vals