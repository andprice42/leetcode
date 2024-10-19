class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        cnt = 1
        fire = None
        for pt in points:
            if fire is None:
                fire = pt[1]
            elif fire >= pt[1]:
                fire = pt[1]
            elif fire < pt[0]:
                cnt += 1
                fire = pt[1]
        return cnt
            