# Time: O(n)
# Space: O(n)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash = {}
        duplicates = {}

        for i in nums1:
            hash[i] = 1

        for i in nums2:
            if i in hash:
                duplicates[i] = 1

        return list(duplicates.keys())