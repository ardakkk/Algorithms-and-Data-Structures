class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        current = self
        ret = ''
        while current:
            ret += str(current.value)
            current = current.next
        return ret

# Time: O(n)
# Space: O(1)
def rotate_list(list, k):
    length = 0
    current = list

    while current:
        length += 1
        current = current.next

    k = k % length

    fast, slow = list, list

    for _ in range(k):
        fast = fast.next

    while fast.next is not None:
        fast = fast.next
        slow = slow.next

    fast.next = list
    head = slow.next
    slow .next = None

    return head

# order is 1, 2 ,3 ,4

llist = Node(1, Node(2, Node(3, Node(4))))

# order should now be 3, 4, 1, 2

print(rotate_list(llist, 2))