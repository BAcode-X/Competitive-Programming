from typing import List

class Solution:
    def decodeString(self, s: str) -> str:
        nums = []
        val = []
        prev = False
        for i in s:
            if i.isdigit():
                if prev:
                    nums[-1] = nums[-1] * 10 + int(i)
                else:
                    nums.append(int(i))
                prev = True
                continue
            if i == ']':
                n = nums.pop()
                kk = []
                x = val.pop()
                while x != '[':
                    kk.append(x)
                    x = val.pop()
                if len(kk) > 1:
                    kk = kk[::-1]
                val.append(n * ''.join(kk))
            else:
                if not val:
                    val.append(i)
                elif i == '[' or val[-1] == '[':
                    val.append(i)
                else:
                    val[-1] += i
            prev = False
        return ''.join(val)
