# Design and implement a data structure for Least Recently Used (LRU) cache.
# It should support the following operations:
# LRUCache(capacity:int)
# get (key:int)-> int
# put (key:int, value:int) -> None
# See p 63 for more details


# O(1), O(n)) where n is the capacity of the cache
# O(1) because put() and get() use remove_node() and add_tail() which are O(1)
# O(n) in space complexity because we store n nodes in the cache and doubly linked list

# ! The point : it use doubly linked list to keep track of the most recent used nodes AND hash map of size capacity to access the cache in O(1)

from typing import Optional


class DoublyLinkedListNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev: Optional["DoublyLinkedListNode"] = None
        self.next: Optional["DoublyLinkedListNode"] = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap: dict[int, DoublyLinkedListNode] = {}  # Hash map that maps keys to nodes
        # Initialize the head and tail dummy nodes and connect them to each other in a basic two-node doubly linked list
        self.head = DoublyLinkedListNode(-1, -1)
        self.tail = DoublyLinkedListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        # Make this node the most recent used
        # Remove it from its current position and add it to the tail
        self._remove_node(self.hashmap[key])
        self._add_to_tail(self.hashmap[key])
        return self.hashmap[key].val

    def put(self, key: int, value: int) -> None:
        # If a node with this key exists, remove it form linked list (before to add it to tail)
        if key in self.hashmap:
            self._remove_node(self.hashmap[key])
        node = DoublyLinkedListNode(key, value)
        self.hashmap[key] = node

        # Remove the least recently used node if we exceed the capacity
        if len(self.hashmap) > self.capacity:
            del self.hashmap[self.head.next.key]  # type: ignore
            self._remove_node(self.head.next)
        self._add_to_tail(node)

    def _add_to_tail(self, node: Optional[DoublyLinkedListNode]) -> None:
        assert node is not None  # Explicitly tell MyPy node is not None
        prev_node = self.tail.prev
        node.prev = prev_node
        node.next = self.tail
        prev_node.next = node  # type: ignore
        self.tail.prev = node

    def _remove_node(self, node: Optional[DoublyLinkedListNode]) -> None:
        assert node is not None  # Explicitly tell MyPy node is not None
        node.prev.next = node.next  # type: ignore
        node.next.prev = node.prev  # type: ignore

    def __str__(self):
        # Read the values from the cache and print them all
        values = []
        for key, value in self.hashmap.items():
            values.append(str(value.val))
        return f"LRUCache : {' -> '.join(values)}"


if __name__ == "__main__":
    cache = LRUCache(3)
    cache.put(1, 100)
    cache.put(2, 250)
    print(cache.get(2))
    cache.put(4, 300)
    cache.put(3, 200)
    print(cache.get(4))
    print(cache.get(1))
    print(cache)

###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################

# # Design and implement a data structure for Least Recently Used (LRU) cache.
# # It should support the following operations:
# # LRUCache(capacity:int)
# # get (key:int)-> int
# # put (key:int, value:int) -> None
# # See p 63 for more details


# # O(1), O(n)) where n is the capacity of the cache
# # O(1) because put() and get() use remove_node() and add_tail() which are O(1)
# # O(n) in space complexity because we store n nodes in the cache and doubly linked list

# # ! The point : it use doubly linked list to keep track of the most recent used nodes AND hash map of size capacity to access the cache in O(1)

# from __future__ import annotations


# class DoublyLinkedListNode:
#     def __init__(self, key: int, val: int):
#         self.key = key
#         self.val = val
#         self.prev: DoublyLinkedListNode | None = None
#         self.next: DoublyLinkedListNode | None = None


# class LRUCache:
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.hashmap: dict[int, DoublyLinkedListNode] = {}  # Hash map that maps keys to nodes
#         # Initialize the head and tail dummy nodes and connect them to each other in a basic two-node doubly linked list
#         self.head = DoublyLinkedListNode(-1, -1)
#         self.tail = DoublyLinkedListNode(-1, -1)
#         self.head.next = self.tail
#         self.tail.prev = self.head

#     def __str__(self):
#         # Read the values from the cache and print them all
#         values = []
#         for key, value in self.hashmap.items():
#             values.append(str(value.val))
#         return f"LRUCache : {' -> '.join(values)}"

#     def get(self, key: int) -> int:
#         if key not in self.hashmap:
#             return -1
#         # Make this node the most recent used
#         # Remove it from its current position and add it to the tail
#         self._remove_node(self.hashmap[key])
#         self._add_to_tail(self.hashmap[key])
#         return self.hashmap[key].val

#     def put(self, key: int, value: int) -> None:
#         # If a node with this key exists, remove it form linked list (before to add it to tail)
#         if key in self.hashmap:
#             self._remove_node(self.hashmap[key])
#         node = DoublyLinkedListNode(key, value)
#         self.hashmap[key] = node
#         # Remove the least recently used node if we exceed the capacity
#         if len(self.hashmap) > self.capacity:
#             del self.hashmap[self.head.next.key]
#             self._remove_node(self.head.next)
#         self._add_to_tail(node)

#     def _add_to_tail(self, node: DoublyLinkedListNode) -> None:
#         prev_node = self.tail.prev
#         node.prev = prev_node
#         node.next = self.tail
#         prev_node.next = node
#         self.tail.prev = node

#     def _remove_node(self, node: DoublyLinkedListNode) -> None:
#         node.prev.next = node.next
#         node.next.prev = node.prev


# if __name__ == "__main__":
#     cache = LRUCache(3)
#     cache.put(1, 100)
#     cache.put(2, 250)
#     print(cache.get(2))
#     cache.put(4, 300)
#     cache.put(3, 200)
#     print(cache.get(4))
#     print(cache.get(1))
#     print(cache)

###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################

# # Design and implement a data structure for Least Recently Used (LRU) cache.
# # It should support the following operations:
# # LRUCache(capacity:int)
# # get (key:int)-> int
# # put (key:int, value:int) -> None
# # See p 63 for more details


# # O(1), O(n)) where n is the capacity of the cache
# # O(1) because put() and get() use remove_node() and add_tail() which are O(1)
# # O(n) in space complexity because we store n nodes in the cache and doubly linked list

# # ! The point : it use doubly linked list to keep track of the most recent used nodes AND hash map of size capacity to access the cache in O(1)

# class DoublyLinkedListNode:
#     def __init__(self, key: int, val: int):
#         self.key = key
#         self.val = val
#         self.prev = None
#         self.next = None

# class LRUCache:
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.hashmap: dict[int, DoublyLinkedListNode] = {}  # Hash map that maps keys to nodes
#         # Initialize the head and tail dummy nodes and connect them to each other in a basic two-node doubly linked list
#         self.head = DoublyLinkedListNode(-1, -1)
#         self.tail = DoublyLinkedListNode(-1, -1)
#         self.head.next = self.tail
#         self.tail.prev = self.head

#     def get(self, key: int) -> int:
#         if key not in self.hashmap:
#             return -1
#         # Make this node the most recent used
#         # Remove it from its current position and add it to the tail
#         self._remove_node(self.hashmap[key])
#         self._add_to_tail(self.hashmap[key])
#         return self.hashmap[key].val

#     def put(self, key: int, value: int) -> None:
#         # If a node with this key exists, remove it form linked list (before to add it to tail)
#         if key in self.hashmap:
#             self._remove_node(self.hashmap[key])
#         node = DoublyLinkedListNode(key, value)
#         self.hashmap[key] = node
#         # Remove the least recently used node if we exceed the capacity
#         if len(self.hashmap) > self.capacity:
#             del self.hashmap[self.head.next.key]
#             self._remove_node(self.head.next)
#         self._add_to_tail(node)

#     def _add_to_tail(self, node: DoublyLinkedListNode) -> None:
#         prev_node = self.tail.prev
#         node.prev = prev_node
#         node.next = self.tail
#         prev_node.next = node
#         self.tail.prev = node

#     def _remove_node(self, node: DoublyLinkedListNode) -> None:
#         node.prev.next = node.next
#         node.next.prev = node.prev

#     def __str__(self):
#         # Read the values from the cache and print them all
#         values = []
#         for key, value in self.hashmap.items():
#             values.append(str(value.val))
#         return f"LRUCache : {' -> '.join(values)}"


# if __name__ == "__main__":
#     cache = LRUCache(3)
#     cache.put(1, 100)
#     cache.put(2, 250)
#     print(cache.get(2))
#     cache.put(4, 300)
#     cache.put(3, 200)
#     print(cache.get(4))
#     print(cache.get(1))
#     print(cache)
