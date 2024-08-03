class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        cnt = 0
        for i in range(m+n):
            if j >= n:
                break
            elif cnt >= m and j <= n and nums1[i] == 0:
                nums1[i] = nums2[j]
                j += 1
            elif nums1[i] > nums2[j]:
                for k in range(m+n-1, i, -1):
                    nums1[k] = nums1[k-1]
                nums1[i] = nums2[j]
                j += 1
            else:
                cnt += 1
                