class lnode:
    def __init__(self, val, ind, next):
        self.val = val
        self.ind = ind
        self.next = next

class Solution:
    def trap(self, height: List[int]) -> int:
        ind = 0
        prev = None
        mx = 0
        stk = None
        tot = 0
        for e in height:
            if prev is None:
                prev = e
                ind += 1
                continue
            elif prev > e:
                lnde = lnode(prev, ind, stk)
                stk = lnde
            elif prev < e:
                mx = prev
                while stk and stk.val <= e:
                    tot += (stk.val - mx)*(ind - stk.ind)
                    mx = stk.val
                    stk = stk.next
                if stk:
                    tot += (e - mx)*(ind - stk.ind)
                    mx = e
            if stk is None:
                mx = 0
            ind += 1
            prev = e
        return tot