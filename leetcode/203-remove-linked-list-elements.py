# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Time: O(n) We traversed thru the LinkedList
# Space: O(1) Our current variable only takes up 1 node
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy_head = ListNode("Filler")
        dummy_head.next = head

        current = dummy_head

        while current:
            if current.next and current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return dummy_head.next

