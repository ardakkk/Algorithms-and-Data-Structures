# Time: O(n) | Space: O(1)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        seqIdx = 0

        for letter in t:
            if seqIdx == len(s):
                return True

            if letter == s[seqIdx]:
                seqIdx += 1

        return seqIdx == len(s)

print(Solution().isSubsequence('abc', 'ahbgdc')) # True
print(Solution().isSubsequence('axc', 'ahbgdc')) # False