class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = set()
        for num in nums:
            if num in freq:
                return True
            freq.add(num)
        return False
