# Time: O(n)
# Space: O(n) Our reset() takes up linear space
import random

class Solution:

    def __init__(self, nums):
        self.array = nums
        self.original = list(nums)

    def reset(self):                    # Linear space
        self.array = self.original
        self.original = list(self.original)

        return self.array

    def shuffle(self):
        for i in range(len(self.array)):
            swap_idx = random.randrange(i, len(self.array))
            self.swap(self.array, i, swap_idx)

        return self.array

    def swap(self, array, i, j):
        array[i], array[j] = array[j], array[i]

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()