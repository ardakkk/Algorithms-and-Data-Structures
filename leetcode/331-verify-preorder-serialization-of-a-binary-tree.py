# Time: 0(n) We go over every character in Input String
# Space: O(n) Splitting the string into an Array takes up memory
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        p = preorder.split(',')
        slots = 1

        for node in p:
            slots -= 1

            if slots < 0:
                return False

            if node != "#":
                slots += 2

        return slots == 0