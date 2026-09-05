# https://leetcode.com/problems/design-hashmap/description/?q=Design+HashMap

class MyHashMap:

    def __init__(self, cap=10):
        self.cap = cap
        self.hms = [[] for _ in range(self.cap)]
      

    def _hash(self, key):
        return key % self.cap

    def put(self, key: int, value: int) -> None:
        if isinstance(key, int) and isinstance(value, int):
            index = self._hash(key)
            hm = self.hms[index]

            for i, (k, v) in enumerate(hm):
                if k == key:
                    hm[i] = (k, value)
                    return

            hm.append((key, value))
            
    def get(self, key: int) -> int:
        index = self._hash(key)
        hm = self.hms[index]
        for k, v in hm:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        index = self._hash(key)
        hm = self.hms[index]
        for i, (k, _) in enumerate(hm):
            if k == key:
                hm.pop(i)
                return
