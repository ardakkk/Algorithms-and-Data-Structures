# Given two strings s and t , write a function to determine if t is an anagram of s.
# Example 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
#
# Input: s = "rat", t = "car"
# Output: false

# Time: O(n) | Space: O(1)
# Our hash table will have 26 key-value pairs at most
class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        s_char_counts = {}  # {l:2, o:1}

        for s_char in s:
            if s_char not in s_char_counts:
                s_char_counts[s_char] = 1
            else:
                s_char_counts[s_char] += 1

        for t_char in t:
            if t_char not in s_char_counts or s_char_counts[t_char] == 0:
                return False
            else:
                s_char_counts[t_char] -= 1

        return True

