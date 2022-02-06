"""
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
    determine if the input string is valid.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n % 2 != 0:
            return False
        brackets = []
        opened = ["(", "{", "["]
        closed = [")", "}", "]"]
        d = {")": "(", "]": "[", "}": "{"}
        for i in s:
            if i in opened:
                brackets.append(i)
            else:
                if not brackets:
                    return False
                if brackets.pop() != d[i]:
                    return False
        if brackets:
            return False
        return True
