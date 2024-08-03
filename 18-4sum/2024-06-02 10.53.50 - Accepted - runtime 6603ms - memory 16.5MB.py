class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ln = len(nums)
        st = set()
        if len(nums) < 4:
            return []
        for i in range(ln):
            for j in range(i+1, ln):
                for k in range(j+1, ln):
                    sm = nums[i] + nums[j] + nums[k]
                    l = self.binSrch(nums[k+1:], target, sm)
                    if l is not None:
                        st.add((nums[i], nums[j], nums[k], l))
        lst = [list(st1) for st1 in st]
        return lst
                    
    def binSrch(self, nums: List[int], target: int, sm: int) -> int:
        if len(nums) == 0:
            return None

        med = len(nums) // 2
        mid = nums[med]
        nsm = sm + mid

        if nsm == target:
            return mid
        elif nsm < target:
            val = self.binSrch(nums[med+1:], target, sm)
        else:
            val = self.binSrch(nums[:med], target, sm)
        
        if val is None and len(nums) == 2 and nums[0] + sm == target:
            return nums[0]
        else:
            return val


