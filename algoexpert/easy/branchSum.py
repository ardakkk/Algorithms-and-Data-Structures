class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Time: O(n) traversing all the nodes
# Space: O(n) recursion callstacks
def branchSums(root):
    sums = []
    calculateBranchSums(root, 0, sums)
    return sums

def calculateBranchSums(node, runningSum, sums):
    if node is None:
        return False

    runningSum = runningSum + node.value
    if node.left is None and node.right is None:
        sums.append(runningSum)
        return

    calculateBranchSums(node.left, runningSum, sums)
    calculateBranchSums(node.right, runningSum, sums)

node = BinaryTree(1)
node.left = BinaryTree(2)
node.left.left = BinaryTree(4)
node.left.right = BinaryTree(6)
node.right = BinaryTree(3)
node.right.left = BinaryTree(4)
node.right.right = BinaryTree(5)

print(branchSums(node)) # [7, 9, 8, 9]