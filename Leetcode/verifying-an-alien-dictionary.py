from string import ascii_lowercase as al

class Solution:
    def convert(self, x, val):
        d = {}
        i = 0
        for j in range(10, 27):
            d[j] = al[i]
            i += 1
        ans = ''
        for i in x:
            if val[i] > 9:
                ans += str(d[val[i]])
            else:
                ans += str(val[i])
        return ans
    
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        val = {let: ind for ind, let in enumerate(order)}
        print(val)
        tmp = words[:]
        tmp.sort(key=lambda x:self.convert(x, val))
        return True if tmp == words else False
