class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sol = Solution()
        memo = {}
        memo = sol.dynProgHelper(nums, memo)
        vals = [v for k, v in memo.items()]
        return max(vals)
    
    def dynProgHelper(self, nums: List[int], memo: dict[int, int]) -> dict[int, int]:
        if len(nums) == 0:
            return memo
        elif len(nums) == 1:
            memo[0] = 1
            return memo
        ln = len(nums)
        if (memo.get(ln-1) is None):
            memo[ln-1] = 1
            sol = Solution()

            for i in range(1, ln):
                old_memo = memo.copy()
                if memo.get(ln-i-1):
                    for j in range(i, ln):
                        if nums[0] < nums[j] and ((memo.get(ln-1) is None) or ((memo[ln-j-1] + 1) > memo[ln-1])):
                            memo[ln-1] = memo[ln-j-1] + 1
                    return memo
                memo = sol.dynProgHelper(nums[i:], memo)
                if (nums[0] < nums[i] and ((memo.get(ln-1) is None) or ((memo[ln-i-1] + 1) > memo[ln-1]))):
                    memo[ln-1] = memo[ln-i-1] + 1

        return memo


