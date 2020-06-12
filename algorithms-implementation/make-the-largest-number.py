"""
Make the Largest Number
Given a number of integers, combine them so it would create the largest number.

Example:
Input: [17, 7, 2, 45, 72]
Output: 77245217
"""
from functools import cmp_to_key
def largestNum(nums):
    def compare(a, b):
        if str(a) + str(b) < str(b) + str(a):
            return 1
        else:
            return -1

    str_nums = [str(n) for n in sorted(nums, key=cmp_to_key(compare))]
    return "".join(str_nums)
print(largestNum([17, 7, 2, 45, 72]))