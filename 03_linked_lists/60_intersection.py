# Linekd List Intersection

# We'll concatenate lists A+B and B+A
# We'll traverse both simultaneously using two pointers
# ! They will have the same node at the same index (if an intersection exists)

# The intersection HAS NOTHING TO DO with the values of the nodes
# It's about the nodes themselves

# O(n+m), O(1)
from __future__ import annotations


class List_Node:
    def __init__(self, val: int, next: List_Node | None):
        self.val = val
        self.next = next


def linked_list_intersection(head_A: List_Node, head_B: List_Node) -> List_Node | None:
    ptr_A = head_A
    ptr_B = head_B
    while ptr_A != ptr_B:
        ptr_A = ptr_A.next if ptr_A else head_B
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

    node = head_A
    print(f"List A : ", end="")
    while node:
        print(f"{node.val} ->", end=" ")
        node = node.next
    print("None")

    previous_node = head_A.next.next.next
    for v in reversed(list_B):
        node = List_Node(v, previous_node)
        previous_node = node
    head_B = node

    node = head_B
    print(f"List B : ", end="")
    while node:
        print(f"{node.val} ->", end=" ")
        node = node.next
    print("None")

    intersection = linked_list_intersection(head_A, head_B)

    node = intersection
    print(f"Inter  : ", end="")
    while node:
        print(f"{node.val} ->", end=" ")
        node = node.next
    print("None")
