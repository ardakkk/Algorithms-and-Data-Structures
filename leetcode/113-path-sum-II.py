# Time: O(n)
# Space: O(n)
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root is None:
            return

        lst = [root.val]

        return self.pathSumHelper(root, lst, sum, [])

    def pathSumHelper(self, node, lst, sum, res):
        if not node.left and not node.right and node.val == sum:
            res.append(lst)

        if node.left:
            self.pathSumHelper(node.left, lst + [node.left.val], sum - node.val, res)

        if node.right:
            self.pathSumHelper(node.right, lst + [node.right.val], sum - node.val, res)

        return res