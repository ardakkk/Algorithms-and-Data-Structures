class Solution:
    def myAtoi(self, number_str: str) -> int:
        number_str = number_str.strip(' ')
        if len(number_str) > 0:
            if not number_str[0].isnumeric() and not (number_str[0] == '+' or number_str[0] == '-'):
                return 0
            if number_str[0].isnumeric(): number_str = '+' + number_str

            number = ""
            for char in number_str[1:]:
                try:
                    if int(char) > -1:
                        number += char
                except ValueError:
                    break

            if len(number) > 0:
                ans = -(int(number)) if number_str[0] == '-' else int(number)
                if ans > 2 ** 31 - 1:
                    return 2 ** 31 - 1
                elif ans < -(2 ** 31):
                    return -(2 ** 31)
                else:
                    return ans

        return 0
