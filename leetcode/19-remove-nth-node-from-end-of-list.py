# Definition for singly-linked list.

# Time: O(n) We traverse thru the Linked List once.
# Space: O(1) We always use two nodes, regardless of size of LL.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy_head = ListNode("placeholder")
        dummy_head.next = head

        slow = dummy_head
        fast = dummy_head

        for _ in range(n):
            fast = fast.next

        # Move slow and fast up one at a time, until fast is last node
        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy_head.next