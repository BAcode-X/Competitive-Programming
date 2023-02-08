class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i, j = 0, n-1
        while i < j:
            val = numbers[i] + numbers[j]
            if val == target:
                return i+1, j+1
            elif val < target:
                i += 1
            else:
                j -= 1
        return []
