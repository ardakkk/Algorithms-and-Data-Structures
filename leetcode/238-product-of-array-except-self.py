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

# Time: O(n)
# Space: O(1)
class Solution2:
    def productExceptSelf(self, nums):
        res = [1] * len(nums)

        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]

        right = 1

        for i in range(len(nums) - 2, -1, -1):
            right *= nums[i + 1]
            res[i] *= right

        return res

