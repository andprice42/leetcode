class lnde:
    def __init__(self, val: int, mn, nxt):
        self.val = val
        self.min = mn
        self.next = nxt
class MinStack:

    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        if self.head is None:
            nnde = lnde(val, val, None)
        else:
            nnde = lnde(val, self.head.min, self.head)
        if val < nnde.min:
            nnde.min = val  
        self.head = nnde

    def pop(self) -> None:
        self.head = self.head.next

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.head.min
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()