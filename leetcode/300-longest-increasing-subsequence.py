# Given an unsorted array of integers, find the length of longest increasing subsequence.
#
# Example:
#
# Input: [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

# Time: O(n^2) | Space: O(n)
class Solution:
    def lengthOfLIS(self, nums):
        if len(nums) == 0:
            return 0

        dp_subsequence = [1] * len(nums)
        max_so_far = 1

        for j in range(1, len(nums)):
            for i in range(j):
                if nums[j] > nums[i]:
                    dp_subsequence[j] = max(dp_subsequence[i] + 1, dp_subsequence[j])
                    max_so_far = max(max_so_far, dp_subsequence[j])

        return max_so_far