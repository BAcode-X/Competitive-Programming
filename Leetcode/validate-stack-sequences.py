from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n = len(pushed)
        end = 0
        while pushed.__len__() and popped.__len__() and end < n:
            if pushed[end] == popped[0]:
                popped.pop(0)
                pushed.pop(end)
                n -= 1
                if end:
                    end -= 1
            else:
                end += 1
        if popped:
            return False
        else:
            return True