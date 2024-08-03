class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret_rows = []
        i = 0
        while i < numRows:
            if i < 1:
                ret_rows.append([1])
            elif i < 2:
                ret_rows.append([1, 1])
            else:
                nrow = [1]
                prow = ret_rows[-1]
                [nrow.append(prow[j] + prow[j+1]) for j in range(len(prow)-1)]
                nrow.append(1)
                ret_rows.append(nrow)
            i += 1
        return ret_rows


