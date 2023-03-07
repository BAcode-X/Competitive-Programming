from itertools import accumulate as ac

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        pref = [0]*(n+1)
        for i in shifts:
            if i[2]:
                pref[i[0]] += 1
                pref[i[1]+1] -= 1
            else:
                pref[i[0]] -= 1
                pref[i[1]+1] += 1
        ak = list(ac(pref))
        new_s = []
        for i in range(n):
            val = ord(s[i]) + ak[i]
            if val > 122:
                x = 97 + ((val - 97) % 26)
            elif val < 97:
                x = 122 - ((122 - val) % 26)
            else:
                x = val
            new_s.append(chr(x))
        
        return ''.join(new_s)
