# Time: O(n) | Space: O(n)

# Input: "A man, a plan, a canal: Panama"
# Output: True
#
# Input: "race a car"
# Output: False

import string
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [val.lower() for val in s if val not in string.punctuation and val not in string.whitespace]
        return s[:] == s[::-1]

# Time: O(n) | Space: O(1) left and right Pointers take up constant space
class Solution2:
    def isPalindrome(self, s):
        s = re.sub(r'[\W_]', '', s).lower()
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True

print(Solution2().isPalindrome('A man, a plan, a canal: Panama'))
print(Solution2().isPalindrome('race a car'))