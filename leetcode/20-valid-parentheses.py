# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Time: O(n) | Space O(n)
# Space complexity: O(n) in worst case, stack is same length as input string
class Solution:
    def isValid(self, s):
        stack = []
        pairs_hash_map = {"(":")", "{":"}", "[":"]"}

        for char in s:
            if char in pairs_hash_map:
                stack.append(char)
            elif len(stack) == 0 or pairs_hash_map[stack.pop()] != char:
                return False

        return len(stack) == 0