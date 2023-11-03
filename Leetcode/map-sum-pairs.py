class MapSum:

    def __init__(self):
        self.data = {}
        self.prefix_sums = {}

    def insert(self, key: str, val: int) -> None:
        diff = val - self.data.get(key, 0)
        self.data[key] = val

        for i in range(1, len(key) + 1):
            prefix = key[:i]
            self.prefix_sums[prefix] = self.prefix_sums.get(prefix, 0) + diff

    def sum(self, prefix: str) -> int:
        return self.prefix_sums.get(prefix, 0)
