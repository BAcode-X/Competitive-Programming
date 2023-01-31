class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        rev = list(map(lambda x: int(str(x)[::-1]), nums))
        tot = set(nums + rev)
        return len(tot)
