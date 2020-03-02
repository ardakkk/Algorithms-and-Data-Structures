import heapq
import random

# Time: depends on sorting algorithms, quick sort is O(n log n)
# Space: O(log n)
class Solution:
    def findKthLargest(self, nums, k):
        return sorted(nums)[len(nums) - k]

# Time: O(n log n)
# Space: O(n)
class Solution2:
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[-1]

# Solved problem using Quick sort
# Time: O(n log n)
# Space: O(n log n), auxiliary (naive) O(n)
class Solution3:
    def findKthLargest(self, nums, k):
        def helper(list, l, r, index):
            if l == r:
                return list[l]
            pivot_index = random.randint(l, r)

            # move pivot to the beginning of list
            list[l], list[pivot_index] = list[pivot_index], list[l]

            # partiation
            i = l
            for j in range(l + 1, r + 1):
                if list[j] < list[l]:
                    i += 1
                    list[i], list[j] = list[j], list[i]

            # move pivot to the correct location
            list[i], list[j] = list[j], list[i]

            # recursively partiation one side
            if index == i:
                return list[i]
            elif index < i:
                return helper(list, l, i - 1, index)
            else:
                return helper(list, i + 1, r, index)

        return helper(nums, 0, len(nums) - 1, len(nums) - k)

solution = Solution3().findKthLargest([3,2,1,5,6,4], 2)

print(solution)