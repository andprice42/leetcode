class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rw = [1]
        i = 0
        while i < rowIndex:
            if i < 1:
                rw = [1, 1]
            else:
                nrw = [1]
                k = 0
                for j in range(len(rw)-1):
                    k = j + 1
                    nrw.append(rw[j]+rw[k])
                nrw.append(1)
                rw = [l for l in nrw]
            i += 1
        return rw