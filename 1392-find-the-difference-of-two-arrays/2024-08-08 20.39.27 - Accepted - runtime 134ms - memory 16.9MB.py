class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        st1 = set()
        st2 = set()
        [st1.add(num) for num in nums1]
        [st2.add(num) for num in nums2]
        return [[num for num in st1 if num not in st2], [num1 for num1 in st2 if num1 not in st1]]