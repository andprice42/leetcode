class Solution:
    def climbStairs(self, n: int) -> int:
        sol = Solution()
        vist = {}
        steps, vist = sol.dpHelper(n, vist)
        return steps

    def dpHelper(self, n: int, vist: dict[int, int]) -> (int, dict[int, int]):
        if vist.get(n):
            steps = vist[n]
        else:
            if (n > 1):
                sol = Solution()
                steps1, vist = sol.dpHelper(n-1, vist)
                steps2, vist = sol.dpHelper(n-2, vist)
                steps = steps1 + steps2
            else:
                vist[1] = 1
                return (1, vist)
        vist[n] = steps
        return (steps, vist)

            

            
