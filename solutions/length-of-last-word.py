"""
    Given a string s consisting of some words separated by some number of spaces, 
    return the length of the last word in the string.
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new_s = s.rstrip()[::-1]
        word = new_s.split()
        return len(word[0][::-1])
