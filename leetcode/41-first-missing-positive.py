# Time: O(n)
# Space: O(n)
class Solution:
    def firstMissingPositive(self, nums):
        hash = {}

        for n in nums:
            hash[n] = 1

        for i in range(1, len(nums)):
            if i not in hash:
                return i

        return -1

# Using bucket sort
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            # print nums[i], i + 1, nums[nums[i] - 1]
            while nums[i] > 0 and nums[i] <= n and nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        # print nums
        for i in range(n):
            if i + 1 != nums[i]:
                return i + 1
        return n + 1