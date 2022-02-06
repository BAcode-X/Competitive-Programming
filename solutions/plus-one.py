"""
    You are given a large integer represented as an integer array digits, 
    where each digits[i] is the ith digit of the integer. 
    The digits are ordered from most significant to least significant in left-to-right order. 
    The large integer does not contain any leading 0's.

    Increment the large integer by one and return the resulting array of digits.
"""


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        int_val = 0
        p = 0
        for digit in digits[::-1]:
            int_val += digit * (10 ** p)
            p += 1
        new_list = list(str(int_val + 1))
        return new_list
