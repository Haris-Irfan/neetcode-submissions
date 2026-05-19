class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        val = self.cache.get(key, -1)
        if val != -1:
            self.cache.move_to_end(key)

        return val
        

    def put(self, key: int, value: int) -> None:
        if self.cache.get(key, -1) != -1:
            self.cache[key] = value
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)
            self.cache[key] = value
        else:
            self.cache[key] = value

        self.cache.move_to_end(key)