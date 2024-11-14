class lnde:
    def __init__(self, val: tuple, next: Optional['lnde']=None):
        self.val = val
        self.next = next

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bankst = set(bank)
        fq = lnde((startGene, 0))
        tail = fq
        while fq:
            hit_list = []
            fstr = fq.val[0]
            depth = fq.val[1]
            if fstr == endGene:
                return depth
            for v in bankst:
                if sum([1 for i in range(8) if fstr[i] == v[i]]) == 7:
                    tail.next = lnde((v, depth+1))
                    tail = tail.next
                    hit_list.append(v)
            for v in hit_list:
                bankst.remove(v)
            fq = fq.next
        return -1