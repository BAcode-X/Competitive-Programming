from string import ascii_lowercase as lower
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key = list(key)[::-1]
        i = 0
        d = {' ': ' '}
        while key:
            t = key.pop()
            if not d.get(t, None):
                d[t] = lower[i]
                i += 1
        return ''.join(list(map(lambda x: d[x], message)))
