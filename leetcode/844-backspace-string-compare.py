# Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

# Example 1:
#
# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".
# Example 2:
#
# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".
# Example 3:
#
# Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".
# Example 4:
#
# Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".

# Time O(n + m) Where N and M are lengths of Input Strings | Space: O(n + m) From our Stacks
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s_stack = []
        t_stack = []

        for char in S:
            if char == "#":
                if s_stack:
                    s_stack.pop()
            else:
                s_stack.append(char)

        for char in T:
            if char == "#":
                if t_stack:
                    t_stack.pop()
            else:
                t_stack.append(char)

        return s_stack == t_stack