# Given the head of a singly linked list, determine if it is a palindrome.
# 1 -> 2 -> 2 -> 1          True
# 1 -> 2 -> 3 -> 2 -> 1     True
# 1 -> 2 -> 3 -> 4          False

# we only need to compare the first half of the original linked list with the reverse of the second half
# if there are an odd number of elements, we can include the middle node in both halves

# Find the middle of the linked list to get the head of the second half
# Reverse the second half of the linked list from this middle node

# We assume it is acceptable to modify the linked list (here second half is reversed)

from typing import Optional


class List_Node:
    def __init__(self, val: int, next: Optional["List_Node"]):
        self.val = val
        self.next = next


def find_middle(head: Optional[List_Node]) -> Optional[List_Node]:
    slow = head
    fast = head
    while fast and fast.next:
        assert slow is not None  # Explicitly tell MyPy slow is not None
        slow = slow.next
        fast = fast.next.next
    return slow


# See 03_linked_lists\50_reversal_iterative.py
def reverse_list(head: Optional[List_Node]) -> Optional[List_Node]:
    curr_node: Optional[List_Node] = head
    prev_node: Optional[List_Node] = None

    while curr_node:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node
    return prev_node


def palindromic_linked_list(head: Optional[List_Node]) -> bool:
    mid = find_middle(head)
    second_head = reverse_list(mid)
    ptr1 = head
    ptr2 = second_head
    res = True
    while ptr2:
        # Explicitly tell MyPy ptr1 is not None so that it can infer ptr1.val is available
        if ptr1 is None or ptr1.val != ptr2.val:
            res = False
            break
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    return res


list_A = [1, 2, 3, 2, 1]
previous_node = None
for v in reversed(list_A):
    node = List_Node(v, previous_node)
    previous_node = node
head_A = node
print(palindromic_linked_list(head_A))  # True


list_B = [1, 2, 1, 2]
previous_node = None
for v in reversed(list_B):
    node = List_Node(v, previous_node)
    previous_node = node
head_B = node
print(palindromic_linked_list(head_B))  # False


# # Given the head of a singly linked list, determine if it is a palindrome.
# # 1 -> 2 -> 2 -> 1          True
# # 1 -> 2 -> 3 -> 2 -> 1     True
# # 1 -> 2 -> 3 -> 4          False

# # we only need to compare the first half of the original linked list with the reverse of the second half
# # if there are an odd number of elements, we can include the middle node in both halves

# # Find the middle of the linked list to get the head of the second half
# # Reverse the second half of the linked list from this middle node

# # We assume it is acceptable to modify the linked list (here second half is reversed)

# from __future__ import annotations


# class List_Node:
#     def __init__(self, val: int, next: List_Node | None):
#         self.val = val
#         self.next = next


# def find_middle(head: List_Node) -> List_Node:
#     slow = head
#     fast = head
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#     return slow


# # See 03_linked_lists\50_reversal_iterative.py
# def reverse_list(head: List_Node | None) -> List_Node | None:
#     curr_node: List_Node | None = head
#     prev_node: List_Node | None = None

#     while curr_node:
#         next_node = curr_node.next
#         curr_node.next = prev_node
#         prev_node = curr_node
#         curr_node = next_node
#     return prev_node


# def palindromic_linked_list(head: List_Node) -> bool:
#     mid = find_middle(head)
#     second_head = reverse_list(mid)
#     ptr1 = head
#     ptr2 = second_head
#     res = True
#     while ptr2:
#         if ptr1.val != ptr2.val:
#             res = False
#             break
#         ptr1 = ptr1.next
#         ptr2 = ptr2.next
#     return res


# list_A = [1, 2, 3, 2, 1]
# previous_node = None
# for v in reversed(list_A):
#     node = List_Node(v, previous_node)
#     previous_node = node
# head_A = node
# print(palindromic_linked_list(head_A))  # True


# list_B = [1, 2, 1, 2]
# previous_node = None
# for v in reversed(list_B):
#     node = List_Node(v, previous_node)
#     previous_node = node
# head_B = node
# print(palindromic_linked_list(head_B))  # False
