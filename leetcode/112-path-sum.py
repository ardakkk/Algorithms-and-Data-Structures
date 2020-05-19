# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time: O(n)
# Space: O(n)
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        self.hasPathSum = False
        self.hasPathSumHelper(root, 0, sum)

        return self.hasPathSum

    def hasPathSumHelper(self, node, runningSum, sum):
        if node is None:
            return False

        runningSum = runningSum + node.val

        if node.left is None and node.right is None and runningSum == sum:
            self.hasPathSum = True
            return True

        self.hasPathSumHelper(node.left, runningSum, sum)
        self.hasPathSumHelper(node.right, runningSum, sum)