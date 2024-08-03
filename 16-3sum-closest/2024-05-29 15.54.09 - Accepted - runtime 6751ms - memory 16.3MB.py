class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ln = len(nums)
        tgt = None
        for i in range(ln-2):
            for j in range(i+1, ln-1):
                val = self.binSrch(nums[j+1:], nums[i] + nums[j], target)
                if tgt is None:
                    tgt = val
                elif abs(tgt-target) > abs(val-target):
                    tgt = val
        return tgt
    
    def binSrch(self, nums: List[int], ab: int, target: int) -> int:
        if len(nums) == 0:
            return None
        mid = len(nums) // 2
        med = nums[mid]
        sm = med + ab
        if sm == target:
            return sm
        elif sm > target:
            val = self.binSrch(nums[:mid], ab, target)
        else:
            val = self.binSrch(nums[mid+1:], ab, target)
        if val is None and len(nums) == 1:
            return sm
        elif len(nums) == 2:
            mindiff = min(abs(ab+nums[0]-target), abs(ab+nums[1]-target))
            if mindiff == abs(ab+nums[0]-target):
                return ab+nums[0]
            elif mindiff == abs(ab+nums[1]-target):
                return ab+nums[1]
        return val


        
        