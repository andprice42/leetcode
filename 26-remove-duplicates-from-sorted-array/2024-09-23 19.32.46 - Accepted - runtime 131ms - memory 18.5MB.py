class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hitlist = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                hitlist.append(i)
        k = 0
        for i in hitlist:
            del nums[i-k]
            k += 1
        return len(nums)

        