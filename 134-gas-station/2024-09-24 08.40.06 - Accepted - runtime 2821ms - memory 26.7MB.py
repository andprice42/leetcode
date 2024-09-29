class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        if len(gas) == 1 and gas[0] >= cost[0]:
            return 0
        elif len(gas) == 1:
            return -1
        idxmax = None
        mx = None
        for i in range(len(gas)):
            if mx is None:
                idxmax = i
                mx = gas[i] - cost[i]
            elif gas[i] - cost[i] > mx:
                mx = gas[i] - cost[i]
                idxmax = i
        visit = [i for i in range(len(gas))]
        new_visit = visit[idxmax:]
        [new_visit.append(i) for i in visit[:idxmax]]
        visit = new_visit
        ind = visit[0]
        start = visit[0]
        gtank = 0
        cnt = 0
        while cnt < len(gas):
            gtank += gas[ind]
            gtank -= cost[ind]
            if gtank < 0 and visit[1] == idxmax:
                return -1
            elif gtank < 0:
                gtank = 0
                new_visit = visit[1:]
                new_visit.append(visit[0])
                visit = new_visit
                cnt = 0
                start = visit[cnt]
                ind = visit[cnt]
            else:
                cnt += 1
                if cnt < len(visit):
                    ind = visit[cnt]
        return start