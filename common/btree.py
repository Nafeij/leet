from dataclasses import dataclass
from typing import Callable

class BTree[T]:
    _arr: list[T]
    def __init__(self, isLeft: Callable[[T, T], bool], size=1):
        self._arr = [None] * size
        self._isLeft = isLeft

    def _has(self, index: int) -> bool:
        return index < len(self._arr) and self._arr[index] is not None

    def _resize(self, index: int):
        if index >= len(self._arr):
            self._arr += [None] * (index - len(self._arr) + 1)

    def _insert(self, index: int, val: T):
        self._resize(index)
        self._arr[index] = val

    def insert(self, val: T):
        index = 0
        while True:
            if not self._has(index):
                self._insert(index, val)
                return
            elif self._isLeft(val, self._arr[index]):
                index = index * 2 + 1
            else:
                index = index * 2 + 2

    def inorder(self) -> list[T]:
        res: list[T] = []
        stack: list[int] = []
        index = 0
        while stack or self._has(index):
            while self._has(index):
                stack.append(index)
                index = index * 2 + 1
            index = stack.pop()
            res.append(self._arr[index])
            index = index * 2 + 2
        return res

if __name__ == '__main__':
    tree = BTree[int](lambda x, y: x < y)
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(2)
    tree.insert(4)
    tree.insert(6)
    tree.insert(8)
    print(tree.inorder())