# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time: O(n)
# Space: O(1) if Function Call Stack size is not considered, otherwise O(n)
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lower, upper):
            if not node:
                return True

            val = node.val

            if not helper(node.right, val, upper):
                return False

            if not helper(node.left, val, lower):
                return False

            return True

        return helper(root, float("-inf"), float("inf"))

# Time: O(n) We traverse thru every Node in the Tree
# Space: O(1)
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        validity = True

        def helper(node, minimum, maximum):
            nonlocal validity
            if not node or not validity:
                return
            if (minimum is not None and node.val <= minimum) or (maximum is not None and node.val >= maximum):
                validity = False
                return
            helper(node.left, minimum, node.val)
            helper(node.right, node.val, maximum)

        helper(root, None, None)

        return validity