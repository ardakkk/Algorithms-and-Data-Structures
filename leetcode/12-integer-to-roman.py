# Repeatedly take of as many copies of each
# numeral as possible until num is less than the value of that numeral.
# Time - O(n) where n = len(str(num)), the longest num
# equivalent is 8 where one digit maps to 4 chars
# Space: O(n)
class Solution:
    def intToRoman(self, num: int) -> str:
        mapping = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I'),
        ]

        roman = []
        for i, numeral in mapping:
            while num >= i:
                num -= i
                roman.append(numeral)

        return "".join(roman)

print(Solution().intToRoman(3)) # III
print(Solution().intToRoman(54)) # LIV
print(Solution().intToRoman(777)) # DCCLXXVII

