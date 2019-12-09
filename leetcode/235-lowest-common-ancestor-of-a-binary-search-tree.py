# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time: O(n) Worst case, we traverse thru every Node in the Tree.
# Space: O(1) We always use one node, regardless of size of BST.
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        current_node = root

        while current_node:
            if current_node.val < p.val and current_node.val < q.val:
                current_node = current_node.right
            elif current_node.val > p.val and current_node.val > q.val:
                current_node = current_node.left
            else:
                return current_node