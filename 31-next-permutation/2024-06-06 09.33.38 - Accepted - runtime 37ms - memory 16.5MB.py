class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        last = len(nums) - 1
        j = last - 1
        while nums[j] >= nums[j+1]:
            j -= 1
            if j < 0:
                nums.sort()
                return nums
        i = last
        while nums[j] >= nums[i]:
            i -= 1
        nums[j], nums[i] = nums[i], nums[j]
        k = j + 1
        l = last
        while k < l:
            nums[k], nums[l] = nums[l], nums[k]
            k = k + 1
            l = l - 1
        return nums