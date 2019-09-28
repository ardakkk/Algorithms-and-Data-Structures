# Time: O(n) | Space: O(n)

# Input: "A man, a plan, a canal: Panama"
# Output: True
#
# Input: "race a car"
# Output: False

import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [val.lower() for val in s if val not in string.punctuation and val not in string.whitespace]
        return s[:] == s[::-1]

