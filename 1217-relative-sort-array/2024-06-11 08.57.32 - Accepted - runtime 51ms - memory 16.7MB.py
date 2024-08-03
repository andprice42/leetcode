class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        lst = []
        j = 0
        while j < len(arr2):
            cnt = 0
            ln1 = len(arr1)
            hit_list = []
            for i in range(ln1):
                if arr1[i] == arr2[j]:
                    lst.append(arr1[i])
                    cnt += 1
            j += 1
            [arr1.remove(lst[-1]) for i in range(cnt)]
        arr1.sort()
        [lst.append(i) for i in arr1]
        return lst