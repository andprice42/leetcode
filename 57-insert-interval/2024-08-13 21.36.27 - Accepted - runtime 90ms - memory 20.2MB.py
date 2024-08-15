class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        prev = None
        ret_intvs = []
        for intv in intervals:
            if prev is None and newInterval[1] < intv[0]:
                ret_intvs.append(newInterval)
                prev = intv
            elif prev is None:
                prev = intv
            # haven't hit it yet
            # in between
            elif newInterval[0] > prev[1] and newInterval[1] < intv[0]:
                ret_intvs.append(prev)
                ret_intvs.append(newInterval)
                prev = intv
            elif prev[1] < newInterval[0]:
                ret_intvs.append(prev)
                prev = intv
            # first in between prev, second less than next
            elif newInterval[0] <= prev[1] and newInterval[1] < intv[0] and newInterval[1] >= prev[0]:
                prev = [min(prev[0], newInterval[0]), max(prev[1], newInterval[1])]
                ret_intvs.append(prev)
                prev = intv
            # first in between prev, second greater than next
            elif newInterval[0] <= prev[1] and newInterval[1] >= intv[0]:
                prev = [min(prev[0], newInterval[0]), max(intv[1], newInterval[1])]
            else:
                ret_intvs.append(prev)
                prev = intv
            print(ret_intvs)

        if prev is None:
            ret_intvs.append(newInterval)
        # haven't hit it yet
        elif prev[1] < newInterval[0]:
            ret_intvs.append(prev)
            ret_intvs.append(newInterval)
        # first in between prev, second less than next
        elif newInterval[0] <= prev[1] and newInterval[1] >= prev[0]:
            prev = [min(prev[0], newInterval[0]), max(prev[1], newInterval[1])]
            ret_intvs.append(prev)
        else:
            ret_intvs.append(prev)
        return ret_intvs

                    







        