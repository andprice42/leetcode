class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        st = set(nums)
        for i in range(len(nums)+1):
            if i not in st:
                return i
        return None