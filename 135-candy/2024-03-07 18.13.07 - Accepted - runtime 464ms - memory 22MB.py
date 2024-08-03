import queue
class Solution:
    def candy(self, ratings: List[int]) -> int:
        rng = range(len(ratings))
        cdict = {i: 1 for i in rng}
        rq = queue.PriorityQueue()
        [rq.put((ratings[i], i)) for i in rng]
        while (rq.empty() is False):
            qtpl = rq.get()
            rt = qtpl[0]
            i = qtpl[1]
            try:
                if (rt > ratings[i+1] and rt > ratings[i-1] and (cdict[i] <= cdict[i-1] or cdict[i] <= cdict[i+1])):
                    cdict[i] = max(cdict[i-1], cdict[i+1]) + 1
                    continue
            except:
                pass
            try:
                if (rt > ratings[i-1] and cdict[i] <= cdict[i-1]):
                    cdict[i] = cdict[i-1] + 1
                    continue
            except:
                pass
            try:
                if (rt > ratings[i+1] and cdict[i] <= cdict[i+1]):
                    cdict[i] = cdict[i+1] + 1
                    rq.put((ratings[i-1], i-1))
            except:
                pass
        val = 0
        for i in rng:
            val += cdict[i]
        return val