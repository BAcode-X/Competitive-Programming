"""
    Return the index of the first occurrence of needle in haystack, 
    or -1 if needle is not part of haystack.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            return haystack.index(needle)
        except ValueError:
            return -1
