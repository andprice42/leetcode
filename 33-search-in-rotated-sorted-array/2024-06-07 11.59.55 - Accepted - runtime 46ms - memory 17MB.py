class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        k = -1
        if nums[0] > nums[-1]:
            k = self.binSrch(nums, target, True, True, None, 0)
            if k is None:
                k = self.binSrch(nums, target, True, False, None, 0)
        botind = 0
        if k is None:
            return -1
        if k > 0:
            left = nums[:k]
            right = nums[k:]
            if left[0] > target:
                nums = right
                botind = k
            else:
                nums = left
        i = self.binSrch(nums, target, False, False, None, botind)
        if i is None:
            i = -1
        return i

    def binSrch(self, nums: List[int], t: int, k: bool, dirc: bool, prevmid: int, botind: int) -> int:
        if len(nums) == 0:
            return None
        mid = len(nums) // 2
        med = nums[mid]
        if k:
            if len(nums) == 1:
                return None
            elif len(nums) == 2 and med > nums[mid-1]:
                return None
            elif med < nums[mid-1]:
                return botind + mid
            elif len(nums) >= 3 and med > nums[mid+1]:
                return botind + mid + 1
            elif prevmid:
                if dirc is False and prevmid < med:
                    dirc = True
                    return self.binSrch(nums[mid:], t, k, dirc, med, botind+mid)
                elif dirc and prevmid > med:
                    dirc = False
                    return self.binSrch(nums[:mid+1], t, k, dirc, med, botind)
                elif dirc:
                    return self.binSrch(nums[mid:], t, k, dirc, med, botind+mid)
                else:
                    return self.binSrch(nums[:mid+1], t, k, dirc, med, botind)
            elif dirc:
                return self.binSrch(nums[mid:], t, k, dirc, med, botind+mid)
            else:
                return self.binSrch(nums[:mid+1], t, k, dirc, med, botind)
        else:
            if med == t:
                return botind + mid
            elif med < t:
                return self.binSrch(nums[mid+1:], t, False, False, med, botind+mid+1)
            else:
                return self.binSrch(nums[:mid], t, False, False, med, botind)
        

