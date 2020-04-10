# Time: O(n)
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i]+nums[i-1])
        return max(nums)

print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

# Time: O(n)
# Space: O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        res = [0]
        currentMax = 0

        for n in nums:
            if currentMax + n < 0:
                currentMax = 0
                res = max(n, res)
            else:
                currentMax += n
                res = max(currentMax, res)
        return res