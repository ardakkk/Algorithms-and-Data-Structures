class Solution:
    def searchRange(self, nums, target):
        first = self.binarySearch(nums, 0, len(nums) - 1, target, True)
        last = self.binarySearch(nums, 0, len(nums) - 1, target, False)
        
        return [first, last]
    
    def binarySearch(self, nums, low, high, target, findFirst):
        if high < low:
            return -1

        mid = low + (high - low) // 2

        if findFirst:
            if ((mid == 0 or target > nums[mid - 1]) and nums[mid] == target):
                return mid
            elif (target > nums[mid]):
                return self.binarySearch(nums, (mid + 1), high, target, findFirst)
            else:
                return self.binarySearch(nums, low, (mid - 1), target, findFirst)
        else:
            if ((mid == len(nums) - 1 or target < nums[mid + 1]) and nums[mid] == target):
                return mid 
            elif (target < nums[mid]):
                return self.binarySearch(nums, low, (mid - 1), target, findFirst)
            else:
                return self.binarySearch(nums, (mid + 1), high, target, findFirst)

arr = [1, 3, 3, 5, 7, 9, 9, 10, 12]
x = 9

solution = Solution()
print(solution.searchRange(arr, x))