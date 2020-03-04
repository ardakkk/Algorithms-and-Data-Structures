import collections

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Time: O(n)
# Space: O(n)
class Solution:
    def removeZeroSumSublists(self, head):
        curr = dummy = ListNode(0)
        dummy.next = head
        prefix = 0
        seen = collections.OrderedDict()

        while curr:
            prefix += curr.val

            if prefix not in seen:
                seen[prefix] = curr
            else:
                node = seen[prefix]
                node.next = curr.next
                while list(seen.keys())[-1] != prefix:
                    seen.popitem()
            curr = curr.next

        return dummy.next
