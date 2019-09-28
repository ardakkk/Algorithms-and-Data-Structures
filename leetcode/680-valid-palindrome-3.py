# Time: 0(n) |  Space: O(n)

# Input: "aba"
# Output: True

# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.


def isPalindrom(s):
    i = 0
    j = len(s)-1
    while i < j and s[i] == s[j]:
        i+=1
        j-=1
    return i>=j

class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while i < j and s[i] == s[j]:
                i+=1
                j-=1

        if i<j:
            return isPalindrom(s[i+1:j+1]) or isPalindrom(s[i:j])
        return True