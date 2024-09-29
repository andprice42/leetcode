class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        batch = (2*numRows-2)
        ln = len(s)
        ret_str = ''.join([s[i] for i in range(0, ln, batch)])
        for j in range(1, numRows-1):
            for k in range(j, ln, batch):
                ret_str += s[k]
                if (k+(batch-2*j) < ln):
                    ret_str += s[k+(batch-2*j)]
            
        for i in range(numRows-1, ln, batch):
            ret_str += s[i]
        return ret_str