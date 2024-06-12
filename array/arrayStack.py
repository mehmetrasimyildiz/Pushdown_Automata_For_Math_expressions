from typing import List, Generic, TypeVar

T = TypeVar('T')


class array_stack(Generic[T]):
    def __init__(self, capacity: int = 10):
        self.stack: List[T] = [None] * capacity
        self.count: int = 0

    def push(self, item: T) -> None:
        if item is None:
            print("Söz dizimi hatalı")
        if self.count >= len(self.stack) - 1:
            temp = [None] * (len(self.stack) * 2)
            for i in range(len(self.stack)):
                temp[i] = self.stack[i]
            self.stack = temp
        self.stack[self.count] = item
        self.count += 1

    def pop(self) -> T:
        if self.count == 0:
            pass
        self.count -= 1
        ret = self.stack[self.count]
        self.stack[self.count] = None
        return ret

    def peek(self) -> T:
        ret = self.pop()
        self.push(ret)
        return ret

    def is_empty(self) -> bool:
        return self.count == 0

    def clear(self) -> None:
        self.count = 0
        self.stack = [None] * len(self.stack)

    def __str__(self) -> str:
        sb = ""
        for i in range(self.count - 1, -1, -1):
            sb += str(self.stack[i]) + " "
        return sb.strip()
