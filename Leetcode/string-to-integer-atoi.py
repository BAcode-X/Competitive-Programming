class Solution:
    def myAtoi(self, s: str) -> int:
        t = ''
        s = s.strip()
        true_s = '0'
        for i in s:
            if i in ['-', '+']:
                if t:
                    break
                else:
                    t = i
            elif i.isdigit():
                if not t:
                    t = '+'
                true_s += i
            else:
                break
        if int(true_s) > 2147483648 and t == '-':
            true_s = f'{2147483648}'
        elif int(true_s) > 2147483647 and t == '+':
            true_s = f'{2147483647}'
        ans = int(t+true_s)
        return ans
