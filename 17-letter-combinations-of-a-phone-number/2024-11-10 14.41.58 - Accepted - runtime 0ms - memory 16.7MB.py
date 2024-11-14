class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letmap = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
        ret_arr = []
        if len(digits) > 0:
            ln0 = len(letmap[int(digits[0])])
        ln = 0
        first = True
        prevln = None
        for dig in digits:
            ln += 1
            num = int(dig)
            for c in letmap[num]:
                if first:
                    ret_arr.append(c)
                else:
                    i = 0
                    for sub in ret_arr:
                        if len(ret_arr[i]) == ln - 1:
                            ret_arr.append(sub + c)
                        i += 1
            if prevln:
                ret_arr = ret_arr[prevln:]
            prevln = len(ret_arr)
            first = False
        
        return ret_arr