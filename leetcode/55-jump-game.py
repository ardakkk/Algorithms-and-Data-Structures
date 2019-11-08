# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Determine if you are able to reach the last index.
#
# Example 1:
#
# Input: [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Time: O(n^2) | Space: O(n) DP array same size as Input Array
# Dynamic programming solution
class Solution:
    def canJump(self, nums):
        dp_positions = [False] * len(nums)
        dp_positions[0] = True

        for j in range(1, len(nums)):
            for i in range(j):
                if dp_positions[i] and i + nums[i] >= j:
                    dp_positions[j] = True

        return dp_positions[-1]

# Time: O
class Solution2:
    def canJump(self, nums):
        max_reach = 0
        for current_step in range(len(nums)):
            if current_step > max_reach:
                return False

            current_reach = current_step + nums[current_step]
            max_reach = max(max_reach, current_reach)

        return True