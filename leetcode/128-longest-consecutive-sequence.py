# Time: O(n) | Space: O(n) We used a hash table to store the O(n) numbers
class Solution:
    def longestConsecutive(self, nums):
        longest_streak = 0

        num_set = {}

        for num in nums:
            if num not in num_set:
                num_set[num] = True

        for num in nums:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(current_streak, longest_streak)

        return longest_streak