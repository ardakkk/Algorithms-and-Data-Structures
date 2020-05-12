# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time: O(n)
# Space: O(n)
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original:
            return None

        if original == target:
            return cloned

        if original.left and cloned.left:
            found = self.getTargetCopy(original.left, cloned.left, target)
            if found:
                return found
        if original.right and cloned.right:
            found = self.getTargetCopy(original.right, cloned.right, target)
            if found:
                return found
