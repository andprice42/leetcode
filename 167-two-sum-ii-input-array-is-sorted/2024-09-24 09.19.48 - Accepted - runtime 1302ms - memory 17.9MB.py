class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)-1, -1, -1):
            j = self.binSrch(numbers[i+1:], target, i+1, numbers[i])
            if j:
                return [i+1, j+1]
        return []
    def binSrch(self, numbers: List[int], target: int, botInd: int, sm: int) -> int:
        if len(numbers) == 0:
            return None
        mid = len(numbers)//2
        med = numbers[mid]
        if med + sm == target:
            return botInd + mid
        elif med + sm > target:
            return self.binSrch(numbers[:mid], target, botInd, sm)
        else:
            return self.binSrch(numbers[mid+1:], target, botInd+mid+1, sm)
