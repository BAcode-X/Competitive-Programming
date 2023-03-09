class DataStream:

    def __init__(self, value: int, k: int):
        self.stream = []
        self.length = 0
        self.value = value
        self.cont = 0
        self.k = k

    def consec(self, num: int) -> bool:
        self.stream.append(num)
        self.length += 1
        if self.value == num:
            self.cont += 1
        else:
            self.cont = 0
        if self.length < self.k:
            return False
        if self.k <= self.cont:
            return True
