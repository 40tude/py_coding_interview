# Reverse a linked list recursively

# Complexity Analysis
#   Time  : O(n)
#   Space : O(n)
# En complexité on est en O(n) car on parcourt la liste une seule fois
# En espace, O(n) car on empile les élément sur la stack du PC
from __future__ import annotations


class List_Node:
    def __init__(self, val: int, next: List_Node | None):
        self.val = val
        self.next = next


def reverse_list(head: List_Node | None) -> List_Node | None:
    # Base cases
    # Si la liste est vide ou si elle ne contient qu'un seul élément y a rien à faire
    if not head or not head.next:
        return head
    # 1
    # On veut commencer par régler le sous problème
    # Donc on inverse la list dont la tête est head.next
    new_head = reverse_list(head.next)

    # 2
    # Il faut inverser les pointeurs
    # Bien voir que head.next c'est (2) head.next.next c'est (2).next
    # C'est bien lui qu'on veut faire pointer sur head (et plus sur (3))
    head.next.next = head
    # head va se retrouver en fin de liste donc head.next doit pointer sur None
    head.next = None

    # Bien voir que c'est le new-head retourné par reverse_list(head.next)
    return new_head


if __name__ == "__main__":
    head: List_Node | None = List_Node(1, List_Node(2, List_Node(3, List_Node(4, None))))
    head = reverse_list(head)
    while head:
        print(head.val)
        head = head.next
