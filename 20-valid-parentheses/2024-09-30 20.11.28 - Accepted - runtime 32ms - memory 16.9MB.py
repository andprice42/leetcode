class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = None

class Solution:
    def isValid(self, s: str) -> bool:
        pardict = {"(": ")", "{": "}", "[": "]"}
        prev = None
        for i in range(len(s)):
            if pardict.get(s[i]):
                if prev:
                    nd = Node(pardict.get(s[i]))
                    nd.next = prev
                    prev = nd
                else:
                    nd = Node(pardict.get(s[i]))
                    nd.next = prev
                    prev = nd
            else:
                if prev:
                    if s[i] != prev.val:
                        return False
                    prev = prev.next
                else:
                    return False
        if prev:
            return False

        return True

        