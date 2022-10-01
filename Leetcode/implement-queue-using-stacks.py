class MyQueue:

    def __init__(self):
        self.data = []

    def push(self, x: int) -> None:
        self.data.append(x)

    def pop(self) -> int:
        return self.data.pop(0)

    def peek(self) -> int:
        return self.data[0]

    def empty(self) -> bool:
        return False if self.data else True
