class ListNode:
    def __init__(self, val: int, nxt: ListNode):
        self.val = val
        self.next = nxt
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        prev = None
        for i in range(len(nums)):
            if prev is None:
                prev = nums[i]
            elif prev > nums[i]:
                j = i - 1
                while prev > nums[j+1] and j > -1:
                    nums[j] = nums[j+1]
                    nums[j+1] = prev
                    j -= 1
                    prev = nums[j]
                prev = nums[i]
            else:
                prev = nums[i]





