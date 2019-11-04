# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# Note: Given n will be a positive integer.
#
# Example 1:
#
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:
#
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# Time: O(n) Our code loops N times | Space: O(n) Array of size N is used
class Solution:
    def climbStairs(self, n):
        if n <= 3:
            return n

        ways = [0, 1, 2, 3]

        for i in range(4, n + 1):
            ways.append(ways[i - 1] + ways[i - 2])

        return ways.pop()

class Solution:
    def climbStairs(self, n):
        if n == 1:
            return n
        first = 1
        second = 2

        for i in range(3, n + 1):
            third = first + second
            first = second
            second = third

        return second

