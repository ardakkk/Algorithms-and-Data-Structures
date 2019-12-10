# Time: 0(n) We go over every character in Input String
# Space: O(n) Splitting the string into an Array takes up memory
# class Solution:
#     def isValidSerialization(self, preorder: str) -> bool:
#         p = preorder.split(',')
#         slots = 1
#
#         for node in p:
#             slots -= 1
#
#             if slots < 0:
#                 return False
#
#             if node != "#":
#                 slots += 2
#
#         return slots == 0

# Time: O(n) We go over every character in Input String
# Space: O(1)
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slots = 1

        for i in range(len(preorder)):
            char = preorder[i]

            if char == ",":
                slots -= 1

                if slots < 0:
                    return False

                prev_char = preorder[i - 1]

                if prev_char != "#":
                    slots += 2

        if preorder[-1] == "#":
            slots -= 1
        else:
            slots += 1

        return slots == 0