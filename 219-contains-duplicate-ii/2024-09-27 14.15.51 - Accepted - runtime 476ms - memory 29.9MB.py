class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dct = {}
        ln = len(nums)
        for i in range(ln):
            if dct.get(nums[i]) is not None and i - dct.get(nums[i]) <= k:
                return True
            else:
                dct[nums[i]] = i
        return False