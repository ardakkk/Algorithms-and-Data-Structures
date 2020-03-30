# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Time: O(n + m)
# Space: O(1)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        def length(head):
            if not head:
                return 0
            return 1 + length(head.next)

        lenA, lenB = length(headA), length(headB)
        currA, currB = headA, headB

        if lenA > lenB:
            for _ in range(lenA-lenB):
                currA = currA.next
        else:
            for _ in range(lenB-lenA):
                currB = currB.next

        while currA != currB:
            currA = currA.next
            currB = currB.next

        return currA