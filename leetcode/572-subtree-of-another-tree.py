# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time: O(N * M):
# Space: O(N)
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        def same_tree(p, q):
            if p and q:
                return p.val == q.val and same_tree(p.left, q.left) and same_tree(p.right, q.right)
            return p == q

        stack = [s]

        while stack:
            popped = stack.pop()

            if same_tree(popped, t):
                return True
            if popped.left:
                stack.append(popped.left)
            if popped.right:
                stack.append(popped.right)

        return False

