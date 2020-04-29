# Given a string, find the length of the longest substring without repeating characters.

# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Time: O(n) | Space: O(min(m, n)).
# Space complexity: O(min(m, n)) The number of keys in Hash Map is bounded by the size of the string n and the size of the charset/alphabet m.
class Solution:
    def lengthOfLongestSubstring(self, s):
        char_map = {}
        max_length = 0
        window_start = 0

        for i in range(len(s)):
            end_char = s[i]

            if end_char in char_map and char_map[end_char] >= window_start:
                window_start = char_map[end_char] + 1

            char_map[end_char] = i
            max_length = max(max_length, i - window_start + 1)


        return max_length


class Solution2:
    def lengthOfLongestSubstring(self, s):
        letters = {}
        tail = -1
        head = 0
        result = 0

        while head < len(s):
            if s[head] in letters:
                tail = max(tail, letters[s[head]])
            letters[s[head]] = head
            result = max(result, head-tail)
            head += 1
        return result