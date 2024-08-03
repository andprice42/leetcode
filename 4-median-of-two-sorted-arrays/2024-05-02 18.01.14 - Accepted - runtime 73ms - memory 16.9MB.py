class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        ln = m+n-1
        mod = ln % 2
        med1 = int((ln-mod)/2)
        med2 = int((ln+mod)/2)
        nums3 = nums1 + nums2
        nums3.sort()
        if mod == 0:
            return nums3[med1]
        else:
            return (nums3[med1]+nums3[med2])/2




        
        

                




            