# Sort the array. For each strings index bidirectional
# search in the rest of the array.
# Time: O(n**2)
# Space: O(1)
class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        res = sum(nums[:3])

        for i in range(len(nums) - 2):
            s = i + 1
            e = len(nums) - 1

            while s < e:
                sumhere = nums[i] + nums[s] + nums[e]
                if abs(sumhere-target) < abs(res - target):
                    res = sumhere
                if sumhere < target:
                    s += 1
                else:
                    e -= 1

        return res


print(Solution().threeSumClosest([-1, 2, 1, -4], 1)) # The sum that is closest to the target is 2. (-1 + 2 + 1 = 2