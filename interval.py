from typing import Callable, List, TypeVar
from dataclasses import dataclass
from common.btree import BTree

# Interval Tree

class IntvTree:
    @dataclass(slots=True)
    class Node:
        interval: tuple[int, int]
        max_end: int

    _btree: BTree['IntvTree.Node']

    def __init__(self):
        def compare(x: IntvTree.Node, y: IntvTree.Node) -> bool:
            if y.max_end < x.interval[1]:
                y.max_end = x.interval[1]
            return x.interval[0] < y.interval[0]
        self._btree = BTree(compare)

    def insert(self, interval: tuple[int, int]):
        node = self.Node(interval, interval[1])
        self._btree.insert(node)

    def inorder(self) -> List[tuple[int, int]]:
        return [node.interval for node in self._btree.inorder()]

    def search(self, interval: tuple[int, int]) -> List[tuple[int, int]]:
        res: List[tuple[int, int]] = []
        stack: List[IntvTree.Node] = []
        nodes = self._btree.inorder()
        for node in nodes:
            if not stack or node.interval[0] <= stack[-1].max_end:
                stack.append(node)
            else:
                stack.pop()
            if stack and not (interval[1] < node.interval[0] or interval[0] > node.interval[1]):
                res.append(node.interval)
        return res


if __name__ == '__main__':
    tree = IntvTree()
    tree.insert((1, 3))
    tree.insert((2, 4))
    tree.insert((5, 7))
    tree.insert((6, 8))
    tree.insert((9, 11))
    tree.insert((10, 12))
    print(tree.inorder())

    print(tree.search((4, 6)))