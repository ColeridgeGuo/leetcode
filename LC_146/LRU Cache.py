"""
Design a data structure that follows a Least Recently Used (LRU) cache.

Implement the LRUCache class:

- LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
- int get(int key)
    Return the value of the key if the key exists, otherwise return -1.
- void put(int key, int value)
    Update the value of the key if the key exists.
    Otherwise, add the key-value pair to the cache.
    If over the capacity, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.
"""
from common_funcs import listToString, stringToList


class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        existing = self.cache.get(key)
        if not existing:
            return -1
        self._remove_node(existing)
        self._move_to_MRU(existing)
        return existing.value

    def put(self, key: int, value: int) -> None:
        existing = self.cache.get(key)
        if existing:
            existing.value = value
            self._remove_node(existing)
            self._move_to_MRU(existing)
            return
        new_node = Node(key, value)
        self.cache[key] = new_node
        self._move_to_MRU(new_node)
        if len(self.cache) > self.capacity:
            lru = self.head.next
            self._remove_node(lru)
            del self.cache[lru.key]

    def _remove_node(self, node: Node) -> None:
        node.prev.next, node.next.prev = node.next, node.prev

    def _move_to_MRU(self, node: Node) -> None:
        mru = self.tail.prev
        mru.next = node
        node.prev = mru
        node.next = self.tail
        self.tail.prev = node


def main():
    while True:
        try:
            operations = stringToList(input())
            arguments = stringToList(input())

            lru_cache = None
            results = []
            for i, operation in enumerate(operations):
                if operation == "LRUCache":
                    lru_cache = LRUCache(arguments[i][0])
                    results.append(None)
                elif operation == "get":
                    results.append(lru_cache.get(arguments[i][0]))
                elif operation == "put":
                    lru_cache.put(*arguments[i])
                    results.append(None)

            out = listToString(results)
            print(out)
        except EOFError:
            break


if __name__ == '__main__':
    main()
