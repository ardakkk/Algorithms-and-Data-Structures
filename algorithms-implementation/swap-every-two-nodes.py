"""
Swap Every Two Nodes in a Linked List

Given a linked list, swap the position of the 1st and 2nd node, then swap the position of the 3rd
and 4th node etc.
"""
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"{self.value}, ({self.next.__repr__()})"

# Time: O(n)
# Space: O(1)
def swap_every_two(llist):
    head = llist

    curr = head


    while curr is not None and curr.next is not None:
        curr.value, curr.next.value = curr.next.value, curr.value
        curr = curr.next.next

    return head

llist = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(swap_every_two(llist))