# Iterate along s, checking if the next 2
# characters match any valid roman numeral.
# If so, add the value of the numeral to the result. Otherwise the next single
# character must match a numeral, which is added to the result.
# Time: O(n)
# Space: O(1)
class Solution:
    def romanToInt(self, s: str) -> int:
        doubles = {'CM': 900, 'CD': 400, 'XC': 90, 'XL': 40, 'IX': 9, 'IV': 4}
        singles = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

        integer = 0
        i = 0

        while i < len(s):
            if i < len(s) - 1 and s[i:i + 2] in doubles:
                integer += doubles[s[i:i + 2]]
                i += 2
            else:
                integer += singles[s[i]]
                i += 1

        return integer

print(Solution().romanToInt('D')) # 500
print(Solution().romanToInt('LVIII')) # 58  L = 50, V= 5, III = 3.
print(Solution().romanToInt('MCMXCIV')) # 1994  M = 1000, CM = 900, XC = 90 and IV = 4.