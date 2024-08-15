class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        st = set([0])
        while i < len(nums):
            if set(nums[i:]) == st:
                return nums
            elif nums[i] == 0:
                del nums[i]
                nums.append(0)
                i -= 1
            i += 1
        return nums  