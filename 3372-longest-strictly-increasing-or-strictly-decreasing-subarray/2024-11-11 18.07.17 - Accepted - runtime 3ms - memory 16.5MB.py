class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc = True
        mx = 0
        prev = 0
        cnt = 0
        for n in nums:
            if inc and n > prev:
                cnt += 1
            elif inc:
                if n < prev:
                    cnt = 2
                    inc = False
                else:
                    cnt = 1
                    inc = False
            elif n < prev:
                cnt += 1
            elif n == prev:
                cnt = 1
                inc = False
            elif n > prev:
                cnt = 2
                inc = True
            mx = max(mx, cnt)
            prev = n
        return mx
        