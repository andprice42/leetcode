class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        j = 0
        ln = len(nums)
        prev = nums[0] - 1
        while j < len(nums):
            val = nums[j]
            if val == prev and cnt == 0:
                cnt = 2
            elif val == prev:
                cnt += 1
            else:
                cnt = 0

            if (cnt > 2):
                nums.pop(j)
                j -= 1
            
            prev = val
            j += 1

        k = len(nums)
        [nums.append(0) for i in range(ln-k)]

        return k