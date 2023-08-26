class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        num = 0
        prev_val = 0
        
        for c in reversed(s):
            val = roman[c]
            
            if val < prev_val:
                num -= val
            else:
                num += val
            prev_val = val
        
        return num
