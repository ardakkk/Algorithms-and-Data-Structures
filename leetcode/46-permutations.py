# Using Backtracking Algorithm
# Time: O(!n)
# Space: O(!n)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def permuteHelper(start):
            if start == len(nums) - 1:
                res.append(nums.copy())

            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                permuteHelper(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        permuteHelper(0)

        return res