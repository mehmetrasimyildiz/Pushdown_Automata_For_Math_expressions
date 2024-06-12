from typing import Any, Hashable


class array_dictionary:
    def __init__(self, capacity: int = 10):
        self.keys = [None] * capacity
        self.values = [None] * capacity
        self.count = 0

    def add(self, key: Hashable, value: Any):
        if value is None:
            raise ValueError("değer geçersiz")

        if self.count >= len(self.keys) - 1:
            self.keys = self.keys + [None] * len(self.keys)
            self.values = self.values + [None] * len(self.values)

        self.keys = key
        self.values[self.count] = value
        self.count += 1

    def remove(self, key: Hashable):
        if key is None:
            raise ValueError("değer geçersiz")

        for i in range(self.count):
            if self.keys[i] == key:
                for j in range(i + 1, self.count):
                    self.keys[j - 1] = self.keys[j]
                    self.values[j - 1] = self.values[j]
                self.count -= 1
                return True
        return False

    def contains_key(self, key: Hashable):
        if key is None:
            raise ValueError("değer geçersiz")

        for item in self.keys:
            if item is None:
                return False
            if item == key:
                return True
        return False

    def contains_value(self, value: Any):
        if value is None:
            raise ValueError("değer yok")

        for item in self.values:
            if item == value:
                return True
        return False

    def is_empty(self):
        return self.count == 0

    def clear(self) -> None:
        self.count = 0
        self.keys = [None] * len(self.keys)
        self.values = [None] * len(self.values)

    def __getitem__(self, key: Hashable) -> Any:
        for i in range(len(self.keys)):
            if key == self.keys[i]:
                return self.values[i]
        raise KeyError(key)

    def __setitem__(self, key: Hashable, value: Any) -> None:
        for i in range(len(self.keys)):
            if key == self.keys[i]:
                self.values[i] = value
                return
        raise KeyError(key)
