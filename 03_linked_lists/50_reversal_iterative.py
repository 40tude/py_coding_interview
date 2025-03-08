# Reverse a linked list iteratively


# Complexity Analysis
#   Time  : O(n)
#   Space : O(1)
# En complexité on est en O(n) car on parcourt la liste une seule fois
# En espace, O(1) car l'inversion se fait en place

from __future__ import annotations


class List_Node:
    def __init__(self, val: int, next: List_Node | None):
        self.val = val
        self.next = next


def reverse_list(head: List_Node | None) -> List_Node | None:
    curr_node: List_Node | None = head
    prev_node: List_Node | None = None

    while curr_node:
        # 2
        next_node = curr_node.next

        # 1
        # This is the first line we want to write BUT we need to store the next node before changing the pointer
        # This explain the line above
        curr_node.next = prev_node

        # 3
        # Shifiting the pointers
        prev_node = curr_node
        curr_node = next_node

    return prev_node


if __name__ == "__main__":

    vals = [1, 2, 3, 4]
    previous_node = None  # Initialize the previous_node explicitly
    for v in reversed(vals):
        node = List_Node(v, previous_node)
        previous_node = node
    head = node

    head = reverse_list(head)

    while head:
        print(head.val)
        head = head.next


###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################

# class List_Node:
#     def __init__(self, val, next):
#         self.val = val
#         self.next = next


# def reverse_list(head):
#     curr_node = head
#     prev_node = None

#     while curr_node:
#         # 2
#         next_node = curr_node.next

#         # 1
#         # This is the first line we want to write BUT we need to store the next node before changing the pointer
#         # This explains the line above
#         curr_node.next = prev_node

#         # 3
#         # Shifting the pointers
#         prev_node = curr_node
#         curr_node = next_node

#     return prev_node


# if __name__ == "__main__":
#     head: List_Node | None = List_Node(1, List_Node(2, List_Node(3, List_Node(4, None))))
#     head = reverse_list(head)
#     while head:
#         print(head.val)
#         head = head.next
