from string import ascii_lowercase as al

class Solution:
    def freqAlphabets(self, s: str) -> str:
        val = {ind+1: let for ind, let in enumerate(al)}
        ans = ''
        i = len(s) - 1
        while i > -1:
            if s[i] == '#':
                ans += val[int(s[i-2:i])]
                i -= 3
            else:
                ans += val[int(s[i])]
                i -= 1
        return ans[::-1]
