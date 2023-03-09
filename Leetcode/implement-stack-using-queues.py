
class MyStack:

    def __init__(self):
        self.stack = []
        self.length = 0

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.length += 1

    def pop(self) -> int:
        if self.length:
            self.length -= 1
            return self.stack.pop()

    def top(self) -> int:
        if self.length:
            return self.stack[-1]

    def empty(self) -> bool:
        if self.length:
            return False
        return True
