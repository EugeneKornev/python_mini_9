from collections import deque


class LRUCache:

    def __init__(self, capacity=16):
        self.max_cap = capacity
        self.cap = 0
        self.assoc_arr = dict()
        self.queue = deque(maxlen=capacity)

    def put(self, key, value):
        if key in self.assoc_arr.keys():
            self.assoc_arr[key] = value
        else:
            if self.cap < self.max_cap:
                self.assoc_arr[key] = value
                self.cap += 1
                self.queue.append(key)
            else:
                self.assoc_arr.pop(self.queue.popleft())
                self.assoc_arr[key] = value
                self.queue.append(key)

    def get(self, key):
        if key in self.assoc_arr.keys():
            self.queue.remove(key)
            self.queue.append(key)
            return self.assoc_arr[key]

    def __str__(self):
        return str(self.assoc_arr)


def test0():
    cache = LRUCache(3)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1  # "1" is now the most recently used
    cache.put(3, 3)
    cache.put(4, 16)  # "2" was displaced, as last used
    print(cache)
    assert cache.get(2) is None
    assert cache.get(4) + 9 == cache.get(3) + 22
    cache.put(5, 32)  # "1" was displaced, as last used
    print(cache)


if __name__ == "__main__":
    test0()

