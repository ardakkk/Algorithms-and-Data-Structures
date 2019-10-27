# Given a string s, find the longest palindromic substring in s
# --- Example
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Time: O(n^2) | Space: O(1)
# Time complexity: O(n^2) Since expanding a palindrome around its center could take up to O(n), and we do this for each character.

class Solution:
    def longestPalindrome(self, s):
        res = ""

        for i in range(len(s)):
            current = self.expand_around_middle(s, i - 1, i + 1)
            in_between = self.expand_around_middle(s, i, i + 1)
            res = max(res, current, in_between, key=len)

        return res

    def expand_around_middle(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right]

print(Solution().longestPalindrome('babad'))