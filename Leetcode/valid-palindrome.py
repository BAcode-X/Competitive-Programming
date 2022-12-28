class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = list(s.lower())
        b = [i for i in a if i.isalnum()]
        return b == b[::-1]
