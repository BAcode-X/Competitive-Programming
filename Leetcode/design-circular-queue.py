class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = deque()
        self.length = 0
        self.size = k

    def enQueue(self, value: int) -> bool:
        if self.length < self.size:
            self.queue.append(value)
            self.length += 1
            return True
        return False

    def deQueue(self) -> bool:
        if self.length:
            self.queue.popleft()
            self.length -= 1
            return True
        return False

    def Front(self) -> int:
        if self.length:
            return self.queue[0]
        return -1

    def Rear(self) -> int:
        if self.length:
            return self.queue[-1]
        return -1

    def isEmpty(self) -> bool:
        if self.length:
            return False
        return True

    def isFull(self) -> bool:
        if self.length < self.size:
            return False
        return True
