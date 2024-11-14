class Solution:
    def checkValid(self, parstr: str) -> bool:
        oc = 0
        for c in parstr:
            if c == "(":
                oc += 1
            elif c == ")" and oc > 0:
                oc -= 1
            else:
                return False
        if oc != 0:
            return False
        else:
            return True 
    def generateParenthesis(self, n: int) -> List[str]:
        memo = set()
        memo = self.addPairs(n, memo, '')
        lst = [st for st in memo if len(st) == 2*n and self.checkValid(st)]
        return lst
    
    def addPairs(self, n: int, memo: set(), parstr: str) -> set():
        if n == 0:
            return memo
        np1 = "(" + parstr + ")"
        np2 = "()" + parstr
        np3 = parstr + "()"
        np4 = ")" + parstr + "("
        np5 = ")(" + parstr
        np6 = parstr + ")("
        np7 = "(" + parstr + "("
        np8 = ")" + parstr + ")"
        np9 = "))" + parstr
        np10 = parstr + "))"
        np11 = "((" + parstr
        np12 = parstr + "(("
        if np1 not in memo:
            memo.add(np1)
            memo = self.addPairs(n-1, memo, np1)
        if np2 not in memo:
            memo.add(np2)
            memo = self.addPairs(n-1, memo, np2)
        if np3 not in memo:
            memo.add(np3)
            memo = self.addPairs(n-1, memo, np3)
        if np4 not in memo:
            memo.add(np4)
            memo = self.addPairs(n-1, memo, np4)
        if np5 not in memo:
            memo.add(np5)
            memo = self.addPairs(n-1, memo, np5)
        if np6 not in memo:
            memo.add(np6)
            memo = self.addPairs(n-1, memo, np6)
        if np7 not in memo:
            memo.add(np7)
            memo = self.addPairs(n-1, memo, np7)
        if np8 not in memo:
            memo.add(np8)
            memo = self.addPairs(n-1, memo, np8)
        if np9 not in memo:
            memo.add(np9)
            memo = self.addPairs(n-1, memo, np9)
        if np10 not in memo:
            memo.add(np10)
            memo = self.addPairs(n-1, memo, np10)
        if np11 not in memo:
            memo.add(np11)
            memo = self.addPairs(n-1, memo, np11)
        if np12 not in memo:
            memo.add(np12)
            memo = self.addPairs(n-1, memo, np12)
        return memo