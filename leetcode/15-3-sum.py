# Time: O(n^2) | Space: O(1)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # O(n*log(n))
        ans = []
        for i in range(len(nums) - 2):
            if i >= 1 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    newans = [nums[i], nums[j], nums[k]]
                    if len(ans) == 0:
                        ans.append([nums[i], nums[j], nums[k]])
                    elif newans != ans[-1]:
                        ans.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    j += 1

        return ans

print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))

# Time: O(n^2)
# Space: O(1)
class Solution2:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # two sum
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1
        return res
        # end two sum