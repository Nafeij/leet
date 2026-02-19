# Jane Street: LRU Cache using a Doubly Linked List and Hash Map

from typing import Optional, Dict

class Node[K,T]:
    def __init__(self, key: K, value: T):
        self.key = key # store key to facilitate deletion from cache
        self.value = value
        self.prev: Optional['Node'] = None
        self.next: Optional['Node'] = None

class LRUCache[K,T]:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: Dict[K, Node] = {}
        self.head = Node(None, None)  # Dummy head
        self.tail = Node(None, None)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        prev_node = node.prev
        next_node = node.next
        if prev_node and next_node:
            prev_node.next = next_node
            next_node.prev = prev_node

    def _add_to_front(self, node: Node):
        node.prev = self.head
        node.next = self.head.next
        if self.head.next:
            self.head.next.prev = node
        self.head.next = node

    def get(self, key: K) -> T:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_front(node)
            return node.value
        return None

    def put(self, key: K, value: T) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_front(node)
        else:
            if len(self.cache) >= self.capacity:
                lru_node = self.tail.prev
                if lru_node and lru_node != self.head:
                    self._remove(lru_node)
                    del self.cache[lru_node.key]
            new_node = Node(key, value)
            self._add_to_front(new_node)
            self.cache[key] = new_node

if __name__ == '__main__':
    lru = LRUCache[int, int](2)
    lru.put(1, 1)
    lru.put(2, 2)
    print(lru.get(1))    # returns 1
    lru.put(3, 3)        #      evicts key 2
    print(lru.get(2))    # returns -1 (not found)
    lru.put(4, 4)        #      evicts key 1
    print(lru.get(1))    # returns -1 (not found)
    print(lru.get(3))    # returns 3
    print(lru.get(4))    # returns 4