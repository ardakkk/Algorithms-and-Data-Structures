# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time: O(P + Q) Where P and Q are number of Nodes in Input Trees
# Space: O(1)
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        same_tree = True

        def check_same_node(p, q):
            nonlocal same_tree
            if (not p and not q) or not same_tree:
                return
            elif not p or not q:
                same_tree = False
                return
            elif p.val != q.val:
                same_tree = False

            check_same_node(p.left, q.left)
            check_same_node(p.right, q.right)

        check_same_node(p, q)
        return same_tree