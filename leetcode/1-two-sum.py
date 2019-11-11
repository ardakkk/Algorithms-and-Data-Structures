# Time: O(n) | Space: O(n)
class Solution:
    def twoSum(self, nums, target):
        nums_visited = {} #{ 2 : 0, 7 : 1}

        for i in range(len(nums)):
            num = nums[i]
            complement = target - num

            if complement in nums_visited:
                return [i, nums_visited[complement]]
            else:
                nums_visited[num] = i