class Solution:
    # Time: O(n^2)
    # Space: O(n)
    def intersection(self, nums1, nums2):
        results = {}

        for num in nums1:
            if num in nums2 and num not in results:
                results[num] = 1

        return list(results.keys())

    # Time: O(n)
    # Space: O(n)
    def intersection2(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)

        return [x for x in set1 if x in set2]

    # Time: O(n)
    # Space: O(n)
    def intersection3(self, nums1, nums2):
        hash = {}
        duplicates = {}

        for i in nums1:
            hash[i] = 1
        for i in nums2:
            if i in hash:
                duplicates[i] = 1

        return list(duplicates.keys())
print(Solution().intersection3([4, 9, 5], [9, 4, 9, 8, 4]))