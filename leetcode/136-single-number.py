# Time: O(n)
# Space: O(n)
class Solution:
    def singleNumber(self, nums):
        occurrence = {}
        
        for n in nums:
            occurrence[n] = occurrence.get(n, 0) + 1
            
        for key, value in occurrence.items():
            if value == 1:
                return key

# Using XOR operator
# Time: O(n) 
# Space: O(1)
class Solution2:
    def singleNumber(self, nums):
        unique = 0

        for n in nums:
            unique ^= n
        return unique
