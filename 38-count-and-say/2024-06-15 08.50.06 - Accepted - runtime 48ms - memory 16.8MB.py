class Solution:
    def countAndSay(self, n: int) -> str:
        if n > 1:
            s = self.countAndSay(n-1)
        else:
            return "1"
        
        start = None
        news = ""
        for c in s:
            if start is None:
                start = c
                cnt = 1
            elif c != start:
                news += "{}{}".format(cnt, start)
                start = c
                cnt = 1
            else:
                cnt += 1
        news += "{}{}".format(cnt, start)
        return news
        