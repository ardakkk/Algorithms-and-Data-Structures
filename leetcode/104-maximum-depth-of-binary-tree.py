# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time: O(N)
# Space: O(1)
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        max_depth = 0


        def dive(node, current_depth):
            nonlocal max_depth

            if not node:
                max_depth = max(current_depth - 1, max_depth)
                return
            dive(node.left, current_depth + 1)
            dive(node.right, current_depth + 1)

        dive(root, 1)
        return max_depth

# Time: O(N)
# Space: O(N)
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0

        stack = [[root, 1]]
        max_depth = 0

        while stack:
            curr = stack.pop()
            node = curr[0]
            level = curr[1]

            if node.left:
                stack.append([node.left, level + 1])

            if node.right:
                stack.append([node.right, level + 1])

            max_depth = max(max_depth, level)

        return max_depth



