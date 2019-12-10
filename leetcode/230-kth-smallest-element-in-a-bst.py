# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        data = []

        def traverse(node):
            if node.left:
                traverse(node.left)

            data.append(node.val)

            if node.right:
                traverse(node.right)

        traverse(root)
        return data[k - 1]