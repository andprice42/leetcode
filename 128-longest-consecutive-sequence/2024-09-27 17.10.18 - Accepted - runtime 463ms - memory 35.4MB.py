class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dct = {}
        mx = 1
        for num in nums:
            new = False
            if dct.get(num) is None:
                new = True
            if new:
                if dct.get(num-1):
                    dct[num] = dct[num-1] + 1
                    if dct[num] > mx:
                        mx = dct[num]
                if dct.get(num+1):
                    if dct.get(num):
                        dct[num] += dct[num+1]
                    else:
                        dct[num] = dct[num+1] + 1
                    if dct[num] > mx:
                        mx = dct[num]
                
                if dct.get(num-1):
                    dlta = dct.get(num-1)
                    dct[num-dlta] = dct[num]
                    dct[num-1] = dct[num]
                if dct.get(num+1):
                    dlta = dct.get(num+1)
                    dct[num+dlta] = dct[num]
                    dct[num+1] = dct[num]
                if dct.get(num) is None:
                    dct[num] = 1
        return mx
