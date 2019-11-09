# Time: O(n) loop each element in input Array | Space: O(n) #keys in HT equal to #unique values in input Array
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited_nums = {} # {7: true, 2: true}

        for num in nums:
            if num in visited_nums:
                return True
            else:
                visited_nums[num] = True

        return False
