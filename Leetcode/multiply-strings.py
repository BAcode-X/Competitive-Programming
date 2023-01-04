class Solution:
    def convert(self, num):
        new = 0
        b = 0
        for i in num[::-1]:
            new += (ord(i) - 48) * (10 ** b)
            b += 1
        return new
    
    def multiply(self, num1: str, num2: str) -> str:
        return str(self.convert(num1) * self.convert(num2))
