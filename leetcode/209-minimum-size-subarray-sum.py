# Time: O(l + r)
# Space: O(1)
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        res = float('inf')
        sum = 0
        left = 0
        right = 0

        while right < len(nums):
            sum += nums[right]
            while sum >= s:
                # updating the result
                res = min(res, right - left + 1)
                # increment left pointer
                sum -= nums[left]
                left += 1
            # increment right pointer
            right += 1

        if res == float('inf'):
            return 0
        else:
            return res