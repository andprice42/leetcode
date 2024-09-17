class lnde:
    def __init__(self, val: int, nxt):
        self.val = val
        self.next = nxt

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        tpl = self.dfs(n, set(), k)
        ret_str = ""
        rev = tpl[1]
        for i in range(n-1, -1, -1):
            ret_str += str(rev[i])
        return ret_str

    def dfs(self, n: int, visited: set, kcnt: int) -> tuple:
        if len(visited) == n:
            kcnt -= 1
            return (kcnt, [])
        head = None
        for i in range(1, n+1):
            if i in visited:
                continue
            elif head is None:
                head = lnde(i, None)
                ptr = head
            else:
                nxt = lnde(i, None)
                ptr.next = nxt
                ptr = nxt

        while head:
            visited.add(head.val)
            tpl = self.dfs(n, visited, kcnt)
            kcnt = tpl[0]
            if tpl[0] == 0:
                vlist = tpl[1]
                vlist.append(head.val)
                return (0, vlist)
            visited.remove(head.val)
            head = head.next
        return (kcnt, [])
