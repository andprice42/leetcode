class lnde:
    def __init__(self, val: int, nxt):
        self.val = val
        self.next = nxt

class Solution:
    def calculate(self, s: str) -> int:
        head = lnde('(', None)
        for c in s:
            if c == ")":
                head = self.modStack(head)
            else:
                nnde = lnde(c, head)
                head = nnde
        head = self.modStack(head)
        return int(head.val)
    
    def modStack(self, head):
        val_ops = set(['+', '-'])
        sm = []
        op = True
        i = -1
        while head.val != "(":
            if op is False and head.val not in val_ops and head.val != ' ':
                sm[i] = head.val + sm[i]
            elif head.val not in val_ops and head.val != ' ':
                op = False
                sm.append(head.val)
                i += 1
            elif head.val in val_ops:
                op = True
                sm.append(head.val)
                i += 1
            head = head.next
        head = head.next
        val = 0
        i = len(sm) - 1
        while i >= 0:
            v = sm[i]
            if v == '+':
                val += int(sm[i-1])
                i -= 2
            elif v == '-':
                val -= int(sm[i-1])
                i -= 2
            elif val == 0:
                val = int(v)
                i -= 1
            else:
                i -= 1
        nnde = lnde(str(val), head)
        head = nnde
        return head