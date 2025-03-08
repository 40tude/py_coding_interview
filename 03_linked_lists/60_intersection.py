# Linked List Intersection

# We'll concatenate lists A+B and B+A
# We'll traverse both simultaneously using two pointers
# ! They will have the same node at the same index (if an intersection exists)

# The intersection HAS NOTHING TO DO with the values of the nodes
# It's about the nodes themselves


# Complexity Analysis
#   Time  : O(n+m)
#   Space : O(1)

from typing import Optional


class List_Node:
    def __init__(self, val: int, next: Optional["List_Node"]):
        self.val = val
        self.next = next


def print_linked_list(head: Optional[List_Node], name: str = "List"):
    if not head:
        print(f"{name} : None")
        return

    values = []
    node: Optional[List_Node] = head
    while node is not None:
        values.append(str(node.val))
        node = node.next
    print(f"{name} : {' -> '.join(values)} -> None")


def linked_list_intersection(head_A: List_Node, head_B: List_Node) -> Optional[List_Node]:
    ptr_A: Optional[List_Node] = head_A
    ptr_B: Optional[List_Node] = head_B
    while ptr_A != ptr_B:
        ptr_A = ptr_A.next if ptr_A else head_B  # ! If we reach the end of A, we start traversing B
        ptr_B = ptr_B.next if ptr_B else head_A
    return ptr_A


if __name__ == "__main__":
    list_A = [1, 3, 4, 8, 7, 2]
    list_B = [6, 4]

    previous_node = None
    for v in reversed(list_A):
        node = List_Node(v, previous_node)
        previous_node = node
    head_A = node
    print_linked_list(head_A, "List A")

    previous_node = head_A.next.next.next  # type: ignore
    for v in reversed(list_B):
        node = List_Node(v, previous_node)
        previous_node = node
    head_B = node
    print_linked_list(head_B, "List B")

    intersection = linked_list_intersection(head_A, head_B)
    print_linked_list(intersection, "Intersection")


# # Linked List Intersection

# # We'll concatenate lists A+B and B+A
# # We'll traverse both simultaneously using two pointers
# # ! They will have the same node at the same index (if an intersection exists)

# # The intersection HAS NOTHING TO DO with the values of the nodes
# # It's about the nodes themselves

# # O(n+m), O(1)

# from __future__ import annotations


# class List_Node:
#     def __init__(self, val: int, next: List_Node | None):
#         self.val = val
#         self.next = next


# def print_linked_list(head: List_Node | None, name: str = "List"):
#     if not head:
#         print(f"{name} : None")
#         return

#     values = []
#     node = head
#     while node:
#         values.append(str(node.val))
#         node = node.next
#     print(f"{name} : {' -> '.join(values)} -> None")


# def linked_list_intersection(head_A: List_Node, head_B: List_Node) -> List_Node | None:
#     ptr_A = head_A
#     ptr_B = head_B
#     while ptr_A != ptr_B:
#         ptr_A = ptr_A.next if ptr_A else head_B  # ! If we reach the end of A, we start traversing B
#         ptr_B = ptr_B.next if ptr_B else head_A
#     return ptr_A


# if __name__ == "__main__":
#     list_A = [1, 3, 4, 8, 7, 2]
#     list_B = [6, 4]

#     previous_node = None
#     for v in reversed(list_A):
#         node = List_Node(v, previous_node)
#         previous_node = node
#     head_A = node
#     print_linked_list(head_A, "List A")

#     previous_node = head_A.next.next.next
#     for v in reversed(list_B):
#         node = List_Node(v, previous_node)
#         previous_node = node
#     head_B = node
#     print_linked_list(head_B, "List B")

#     intersection = linked_list_intersection(head_A, head_B)
#     print_linked_list(intersection, "Intersection")
