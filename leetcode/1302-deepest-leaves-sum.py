# BFS
# For each layer, sum all the node values and find all nodes in the next layer.
# the sum of nodes in the previous layer.

# Time: O(n), Space: O(n)
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        nodes = [root]

        while nodes:
            level_sum = 0
            new_nodes = []

            for node in nodes:
                level_sum += node.val
                if node.left:
                    new_nodes.append(node.left)
                if node.right:
                    new_nodes.append(node.right)

            nodes = new_nodes

        return level_sum