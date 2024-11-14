class lnde:
    def __init__(self, val: int, next: Optional['lnde'] = None):
        self.val = val
        self.next = next
class MyStack:

    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, x: int) -> None:
        nnde = lnde(x, self.head)
        self.head = nnde

    def pop(self) -> int:
        ret_val = self.head.val
        self.head = self.head.next
        return ret_val

    def top(self) -> int:
        return self.head.val

    def empty(self) -> bool:
        if self.head:
            return False
        else:
            return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()