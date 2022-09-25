"""
    Given an integer number n, return the difference between the product of its digits and the sum of its digits.
"""

from math import prod

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        l = list(map(int, list(str(n))))
        return prod(l) - sum(l)