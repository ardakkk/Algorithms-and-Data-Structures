# Time: O(n) | Space: O(n) We created two dp arrays, each same length as Input
class Solution:
    def maxProduct(self, nums):
        max_till_index = [nums[0]]
        min_till_index = [nums[0]]
        max_product = nums[0]

        for i in range(1, len(nums)):
             num = nums[i]
             max_till_index.append(max(num, num * max_till_index[i - 1]), num * min_till_index[i - 1])
             min_till_index.append(min(num, num * max_till_index[i - 1]), num * min_till_index[i - 1])
             max_product = max(max_product, max_till_index[i])

        return max_product

