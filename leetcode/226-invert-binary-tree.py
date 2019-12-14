# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time: O(N) We traverse thru ever Node in the Tree.
# Space: O(1)
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        self.helper(root)

        return root

    def helper(self, node):
        if not node:
            return

        temp = node.left
        node.left = node.right
        node.right = temp

        self.helper(node.left)
        self.helper(node.right)