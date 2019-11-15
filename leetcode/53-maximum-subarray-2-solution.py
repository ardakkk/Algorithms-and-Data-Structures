# Time O(n) | Space: O(n)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]]
        result = nums[0]

        for i range(1, len(nums)):
            num = nums[i]
            dp.append(max(num, num + dp[i - 1]))
            result = max(result, dp[i])

        return result

# Time O(n) | Space: O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]

        for i range(1, len(nums)):
            nums[i] = (max(nums[i], nums[i] + dp[i - 1]))
            result = max(result, nums[i])

        return result
