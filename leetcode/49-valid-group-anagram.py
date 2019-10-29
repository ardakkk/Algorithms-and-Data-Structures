# Given an array of strings, group anagrams together.
# Example:
#
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]

# Time: O(n k log k)| Space: O(n k)
# Time complexity: O(N K log K) Where N is # of strings, and K is length of strings
# Space complexity: O(N K) Data stored in our grouped Hash Table
class Solution:
    def groupAnagrams(self, strs):
        grouped = {}

        for word in strs:
            key = "".join(sorted(word))

            if key in grouped:
                grouped[key].append(word)
            else:
                grouped[key] = [word]

        return list(grouped.values())

result = Solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(result)