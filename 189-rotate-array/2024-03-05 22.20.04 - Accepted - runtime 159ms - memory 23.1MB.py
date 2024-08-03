class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        ln = len(nums)
        nums1 = [e for e in nums]
        if k > ln:
            k = k % ln
        for i in range(ln):
            if i < k:
                nums[i] = nums1[ln-k+i]
            else:
                nums[i] = nums1[i-k]        