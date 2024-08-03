class listNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) <= 1:
            return 0
        arr = []
        k = 0
        head = None
        for i in s:
            if i == "(":
                lnd = listNode(k, head)
                arr.append(0)
                head = lnd
            elif head is not None:
                arr[head.val] = 1
                arr.append(1)
                head = head.next
            else:
                arr.append(0)
            k += 1
        cnt = 0
        mxcnt = 0
        for i in arr:
            if i == 1:
                cnt += 1
            elif i == 0:
                cnt = 0
    
            if cnt > mxcnt:
                mxcnt = cnt

        return mxcnt


