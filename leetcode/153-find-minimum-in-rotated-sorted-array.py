# Time: O(Log n) We performed a Binary Search
# Space: O(1)
class Solution:
    def findMin(self, nums):
        if len(nums) == 1:
            return nums[0]
        
        left = 0
        right = len(nums) - 1

        if nums[0] < nums[right]:
            return nums[0]

        while left <= right:
            mid = (right + left) // 2

            mid_val = nums[mid] 
            right_of_mid_val = nums[mid + 1]
            left_of_mid_val = nums[mid - 1]
            
            if mid_val > right_of_mid_val:
                return right_of_mid_val
            
            if left_of_mid_val > mid_val:
                return mid_val

            if mid_val > nums[0]:
                left = mid + 1
            else:
                right = mid - 1

solution = Solution()
print(solution.findMin([3, 4, 5, 1, 2]))