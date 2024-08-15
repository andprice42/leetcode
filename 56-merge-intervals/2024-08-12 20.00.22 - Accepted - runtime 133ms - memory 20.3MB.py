class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        prev = None
        ret_intvs = []
        intervals.sort()
        for iv in intervals:
            if prev is None:
                prev = iv
            elif prev[1] >= iv[0]:
                prev = [prev[0], max(iv[1], prev[1])]
            else:
                ret_intvs.append(prev)
                prev = iv
        ret_intvs.append(prev)
        return ret_intvs