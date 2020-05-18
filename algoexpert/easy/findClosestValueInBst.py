class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Average: O(log(n)) time | O(log(n)) space
# Worst: O(n) time | O(n) space

# def findClosestValueInBst(tree, target):
#     return findClosestValueInBstHelper(tree, target, float("inf"))

# def findClosestValueInBstHelper(tree, target, closest):
#     if tree is None:
#         return closest
#     if abs(target - closest) > abs(target - tree.value):
#         closest = tree.value
#     if target < tree.value:
#         return findClosestValueInBstHelper(tree.left, target, closest)
#     elif target > tree.value:
#         return findClosestValueInBstHelper(tree.right, target, closest)
#     else:
#         return closest

# Average: O(log(n)) time | O(1) space
# Worst: O(n) time | O(1) space

def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, float("inf"))

def findClosestValueInBstHelper(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest

#             9
#           /  \
#          4   17
#         / \    \
#        3   6    22
#           / \   /
#          5   7  20

node = Node(9)
node.left = Node(4)
node.left.left = Node(3)
node.left.right = Node(6)
node.left.right.left = Node(5)
node.left.right.right = Node(7)
node.right = Node(17)
node.right.right = Node(22)
node.right.left = Node(20)

print(findClosestValueInBst(node, 4))  # 4
print(findClosestValueInBst(node, 18)) # 17
print(findClosestValueInBst(node, 12)) # 9