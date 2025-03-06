# Remove Kth last node

# 2 pointers : leader, trailer
# Dummy node to handle case where head is removed
# ! Leader goes k steps ahead
# ! Then move ahead both pointers until leader reaches the end
# Trailer is at the node before the one to remove   T.next = T.next.next
# return Dummy.next

# O(n), O(1)
# # O(n) complexity since we traverse at most n nodes
# O(1) space
from __future__ import annotations


class List_Node:
    def __init__(self, val: int, next: List_Node | None):
        self.val = val
        self.next = next


def remove_kth_lest_node(head: List_Node, k: int) -> List_Node:

    dummy_head = List_Node(-1, head)
    trailer = leader = dummy_head
    for _ in range(k):
        leader = leader.next
        if not leader:
            return head
    while leader.next:
        leader = leader.next
        trailer = trailer.next
    trailer.next = trailer.next.next

    return dummy_head.next


if __name__ == "__main__":
    vals = [42, 2, 4, 7, 9, 10]

    # for i, v in enumerate(vals):
    #     if i == 0:
    #         node = List_Node(vals[len(vals) - i - 1], None)
    #     else:
    #         node = List_Node(vals[len(vals) - i - 1], previous_node)
    #     previous_node = node

    previous_node = None  # Initialize the previous_node explicitly
    for v in reversed(vals):
        node = List_Node(v, previous_node)
        previous_node = node

    head = node
    while head:
        print(head.val)
        head = head.next

    head = node
    head = remove_kth_lest_node(head, 3)

    print()
    while head:
        print(head.val)
        head = head.next
