class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        lst = []
        prev = None
        if len(nums) == 0:
            return lst
        start = nums[0]
        for num in nums:
            if prev is None or num - prev == 1:
                prev = num
                continue
            elif start == prev:
                lst.append(f"{start}")
                start = num
                prev = num
            else:
                lst.append(f"{start}->{prev}")
                start = num
                prev = num
        if start == prev:
            lst.append(f"{start}")
        else:
            lst.append(f"{start}->{prev}")
        return lst