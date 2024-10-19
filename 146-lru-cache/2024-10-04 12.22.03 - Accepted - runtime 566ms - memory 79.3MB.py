class Node:
    def __init__(self, key: int, val: int, next: Optional['Node'] = None, prev: Optional['Node'] = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.mp = {}

    def get(self, key: int) -> int:
        if self.mp.get(key) is None:
            return -1
        else:
            curr_pos = self.mp.get(key)
            prev_pos = curr_pos.prev
            if prev_pos:
                prev_pos.next = curr_pos.next
                if curr_pos.next:
                    curr_pos.next.prev = prev_pos
                else:
                    self.tail = prev_pos
                curr_pos.next = self.head
                curr_pos.prev = None
                self.head.prev = curr_pos
                self.head = curr_pos
                if prev_pos.prev is None:
                    prev_pos.prev = curr_pos
            return self.head.val

    def put(self, key: int, value: int) -> None:
        if self.mp.get(key) is not None:
            nde = self.mp.get(key)
            prev_node = nde.prev
            if prev_node:
                prev_node.next = nde.next
                if prev_node.next is None:
                    self.tail = prev_node
                else:
                    nde.next.prev = prev_node
            else:
                self.head = nde.next
                if self.head:
                    self.head.prev = None
            del self.mp[key]
        elif len(self.mp) == self.capacity:
            new_tail = self.tail.prev
            if new_tail:
                new_tail.next = None
                del self.mp[self.tail.key]
                self.tail = new_tail
            else:
                del self.mp[self.tail.key]
                self.head = None
                self.tail = None
        nnde = Node(key, value, self.head)
        if self.head:
            self.head.prev = nnde
        self.mp[key] = nnde
        self.head = nnde
        if self.tail is None:
            self.tail = nnde

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)