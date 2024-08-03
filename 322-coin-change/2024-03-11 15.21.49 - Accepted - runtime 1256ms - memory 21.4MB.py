class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if (amount == 0):
            return 0
        memo = {amount: -1}
        sol = Solution()
        memo = sol.dynProgHelper(coins, amount, memo)
        return memo[amount]

    def dynProgHelper(self, coins: List[int], amount: int, memo: dict[int, int]) -> dict[int, int]:
        if (amount == 0):
            memo[0] = 0
            return memo
        
        try_list = [amount - i for i in coins if amount - i >= 0]
        sol = Solution()
        minsteps = -1
        for amt in try_list:
            if memo.get(amt) is None:
                memo = sol.dynProgHelper(coins, amt, memo)
            
            if (memo.get(amt) is None or memo.get(amt) == -1):
                memo[amt] = -1
            elif (minsteps is None):
                minsteps = memo[amt] + 1
            elif (minsteps == -1 or minsteps > memo[amt]):
                minsteps = memo[amt] + 1
        memo[amount] = minsteps
        return memo
        
            
        
