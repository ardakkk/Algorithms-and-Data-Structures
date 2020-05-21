class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Time: O(n) n is total number of depth
# Space: O(h) h is height of depth
def nodeDepths(root):
    sumOfDepths = 0
    stack = [{"node": root, "depth": 0}]

    while len(stack) > 0:
        nodeInfo = stack.pop()
        node, depth = nodeInfo['node'], nodeInfo["depth"]

        if node is None:
            continue

        sumOfDepths += depth

        stack.append({"node": node.left, "depth": depth + 1})
        stack.append({"node": node.right, "depth": depth + 1})

    return sumOfDepths

# Time: O(n) n is total number of depth
# Space: O(h) h is height of depth
def nodeDepthRecursion(root, depth = 0):
    if root is None:
        return 0

    return depth + nodeDepthRecursion(root.left, depth + 1) + nodeDepthRecursion(root.right, depth + 1)

bt = BinaryTree(1)
bt.left = BinaryTree(2)
bt.left.left = BinaryTree(4)
bt.left.right = BinaryTree(6)
bt.right = BinaryTree(3)
bt.right.left = BinaryTree(4)
bt.right.right = BinaryTree(5)

print(nodeDepthRecursion(bt))