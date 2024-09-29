class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        big_n = 1
        zero = False
        for num in nums:
            if zero is False and num == 0:
                zero = True
            elif zero and num == 0:
                return [0 for i in range(len(nums))]
            else:
                big_n *= num
        answer = []
        for i in range(len(nums)):
            if zero and nums[i] == 0:
                answer.append(big_n)
            elif zero:
                answer.append(0)
            else:
                answer.append(int(big_n/nums[i]))
        return answer