class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        s = s.replace('()', '1')
        stack = []
        cnt = 0
        for i in s:
            if i != ')':
                stack.append(i)
            else:
                tmp = 0
                while stack and stack[-1] != '(':
                    tmp += int(stack[-1])
                    stack.pop()
                if stack and stack[-1] == '(':
                    stack.pop()
                tmp *= 2
                stack.append(str(tmp))
        while stack:
            cnt += int(stack[-1])
            stack.pop()
        return cnt
