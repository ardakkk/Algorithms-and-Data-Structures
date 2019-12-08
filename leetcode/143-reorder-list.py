# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Time: O(n) We traverse thru input LL multiple times
# Space: O(1)
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        # Find middle node and set it to slow
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Split th LL to two LL with middle node. Revers 2nd half

        second_head = self.reverseList(slow.next)
        slow.next = None

        # Zipper the two together

        current = head
        current2 = second_head

        while current2:
            current_next = current.next
            current2_next = current2.next

            current.next = current2
            current2.next = current_next

            current = current_next
            current2 = current2_next

    def reverseList(self, head):
        prev = None
        current = head

        while current:
            temp = current.next

            current.next = prev

            # move prev and current up by 1 node
            prev = current
            current = temp

        return prev
