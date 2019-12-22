# Time: O(n) We traverse the list containing n elements only once. Each look up in the Hash table costs only O(1) time
# Space: O(n) Number of key value pairs stored in hash table, stores at most n elements
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


class Solution:
    def twoSum(self, nums, target):
        dict = {}
        
        for i, num in enumerate(nums):
            if target - num in dict:
                return [dict[target - num], i]
            dict[num] = i
        return []