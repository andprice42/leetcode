class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        sol = Solution()
        memo = sol.dynProgHelp(m, n, memo)
        return memo[(m, n)]
    def dynProgHelp(self, m, n, memo):
        sol = Solution()
        if memo.get((m, n)):
            return memo
        elif m > 1 and n > 1:
            memo = sol.dynProgHelp(m-1, n, memo)
            memo = sol.dynProgHelp(m, n-1, memo)
            memo[(m, n)] = memo[(m-1, n)] + memo[(m, n-1)]
        elif n > 1:
            memo = sol.dynProgHelp(m, n-1, memo)
            memo[(m, n)] = memo[(m, n-1)]
        elif m > 1:
            memo = sol.dynProgHelp(m-1, n, memo)
            memo[(m, n)] = memo[(m-1, n)]
        else:
            memo[(m, n)] = 1
        return memo

