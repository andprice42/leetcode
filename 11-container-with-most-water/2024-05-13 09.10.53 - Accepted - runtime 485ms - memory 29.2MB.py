class Solution:
    def maxArea(self, height: List[int]) -> int:
        ln = len(height)
        mx = 0
        j = ln - 1
        i = 0
        while j > i:
            cap = (j-i)*min(height[i], height[j])
            if cap > mx:
                mx = cap
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return mx