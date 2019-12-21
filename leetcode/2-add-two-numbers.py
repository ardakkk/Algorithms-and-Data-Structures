# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.addTwoNumbersHelper(l1, l2, 0)
    def addTwoNumbersIterative(self, l1, l2):
        head = node = ListNode(None)
        carry = 0

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            node.next = ListNode(carry % 10)
            node = node.next
            carry //= 10
        return head.next

    def addTwoNumbersHelper(self, l1, l2, c):
        val = l1.val + l2.val + c
        c = val // 10
        ret = Node(val % 10)

        if l1.next != None or l2.next != None:
            if not l1.next:
                l1.next = Node(0)
            if not l2.next :
                l2.next = Node(0)
            ret.next = self.addTwoNumbersHelper(l1.next, l2.next, c)
        return ret
        
l1 = Node(2)
l1.next = Node(4)
l1.next.next = Node(3)

l2 = Node(5)
l2.next = Node(6)
l2.next.next = Node(4)

answer = Solution().addTwoNumbers(l1, l2)
while answer:
    print answer.val
    answer = answer.next