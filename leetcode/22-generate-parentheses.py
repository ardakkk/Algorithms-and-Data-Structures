# Time: O(n)
# Space: O(n)
class Solution:
    def generateParenthesis(self, n):
        res = []

        def backtrack(str, left, right):
            if len(str) == 2 * n:
                res.append(str)
                return
            if left < n:
                backtrack(str + '(', left + 1, right)
            if left > right:
                backtrack(str + ')', left, right + 1)

        backtrack('', 0, 0)
        return res