# Time: O(n)
# SpaceL: O(n)
class Solution:
    def countElements(self, arr: List[int]) -> int
        dict = {}
        result = 0

        for i in arr:
            dict[i] = 1

        for x in arr:
            if x+1 in dict:
                result += 1
        return result