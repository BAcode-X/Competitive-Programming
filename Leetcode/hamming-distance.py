class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = bin(x ^ y)
        return xor[2:].count("1")
