# Time: O(n) | Space: O(1)
class Solution:
    def productExceptSelf(self, nums):
        output = [1] * len(nums)
        cumulative_product = 1

        # Multiply from the left
        for i in range(len(nums)):
            output[i] = output[i] * cumulative_product
            cumulative_product = cumulative_product * nums[i]

        cumulative_product = 1

        # Multiply from the right

        for i in range(len(nums) - 1 , -1, -1):
            output[i] = output[i] * cumulative_product
            cumulative_product = cumulative_product * nums[i]

        return output