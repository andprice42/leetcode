class lnde:
    def __init__(self, val: int, next: Optional['lnde'] = None):
        self.val = val
        self.next = next
class MyQueue:

    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, x: int) -> None:
        if self.head is None:
            nnde = lnde(x)
            self.head = nnde
            self.tail = nnde
        else:
            nnde = lnde(x)
            self.tail.next = nnde
            self.tail = self.tail.next

    def pop(self) -> int:
        ret_obj = self.head.val
        self.head = self.head.next
        return ret_obj

    def peek(self) -> int:
        return self.head.val

    def empty(self) -> bool:
        if self.head:
            return False
        else:
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()