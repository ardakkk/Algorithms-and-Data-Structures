# Reverse a singly linked list.
#
# Example:
#
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Time: O(n) | Space: O(1)
class Solution:
    def reverseList(self, head):
        prev = None

        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp

        return prev