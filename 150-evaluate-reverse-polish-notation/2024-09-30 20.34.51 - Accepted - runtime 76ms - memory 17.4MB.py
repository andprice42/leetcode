class lnde:
    def __init__(self, val: str, nxt: Optional['lnde'] = None):
        self.val = val
        self.next = nxt
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        val_ops = set(['+', '-', '*', '/'])
        i = 0
        head = None
        while i < len(tokens):
            if tokens[i] in val_ops:
                v = self.arith([head.next.val, tokens[i], head.val])
                head = head.next.next
                nnde = lnde(v, head)
                head = nnde
            else:
                nnde = lnde(int(tokens[i]), head)
                head = nnde
            i += 1
        return int(head.val)
    def arith(self, expr: List[str]) -> int:
        num1 = int(expr[0])
        num2 = int(expr[2])
        oper = expr[1]
        if oper == '*':
            return num1 * num2
        elif oper == '/':
            return num1 / num2
        elif oper == '+':
            return num1 + num2
        else:
            return num1 - num2