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

class Node(object):
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
    def __str__(self):
        c = self
        answer = ''
        while c:
            answer += str(c.val) if c.val else ""
            c = c.next
        return answer

def merge(lists):
    arr = []
    for node in lists:
        while node:
            arr.append(node.val)
            node = node.next
    head = root = None
    for val in sorted(arr):
        if not root:
            head = root = Node(val)
        else:
            root.next = Node(val)
            root = root.next
    return head

def merge2(lists):
    head = current = Node(-1)

    while any(list is not None for list in lists):
        current_min, i = min((list.val, i) for i, list in enumerate(lists) if list is not None)
        lists[i] = lists[i].next
        current.next = Node(current_min)
        current = current.next

    return head.next

a = Node(1, Node(3, Node(5)))
b = Node(2, Node(4, Node(6)))

print(a)
print(b)
print(merge2([a, b]))