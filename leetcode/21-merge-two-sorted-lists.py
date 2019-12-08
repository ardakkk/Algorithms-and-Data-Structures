# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#
#         head = sort_list = ListNode(0)
#
#         while (l1 and l2):
#             if (l1.val < l2.val):
#                 sort_list.next = l1
#                 l1 = l1.next
#                 sort_list = sort_list.next
#
#             elif (l1.val >= l2.val):
#                 sort_list.next = l2
#                 l2 = l2.next
#                 sort_list = sort_list.next
#
#         sort_list.next = l1 or l2
#         return head.next

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# Time: O(N + M) Where N and M are length of Linked Lists
# Space: O(1) We always use three nodes, regardless of size of LL
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode("Placeholder")
        tail = dummy_head

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next

            tail = tail.next

        tail.next = l1 or l2

        return dummy_head.next