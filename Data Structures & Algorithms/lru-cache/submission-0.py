class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.queue = deque()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.queue.remove(key)
            self.queue.appendleft(key)
            return self.cache[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.queue.remove(key)
            self.queue.appendleft(key)
        else:
            if len(self.cache) == self.capacity:
                self.cache.pop(self.queue.pop())
            self.cache[key] = value
            self.queue.appendleft(key)
        
