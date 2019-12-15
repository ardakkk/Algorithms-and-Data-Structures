# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time: O(N) We traverse thru every Node in the Tree
# Space: O(1)
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.helper(root, 0, res)

        return res

    def helper(self, node, depth, res):
        if not node:
            return
        if len(res) <= depth:
            res.append([])

        res[depth].append(node.val)
        self.helper(node.left, depth + 1, res)
        self.helper(node.right, depth + 1, res)

