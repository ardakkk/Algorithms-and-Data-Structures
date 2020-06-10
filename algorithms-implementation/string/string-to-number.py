"""
Given a string, convert it to an integer without using the builtin str function. You
are allowed to use ord to convert a character to ASCII code.

Consider all possible cases of an integer. In the case where the string is not a
valid integer, return None

"""

# Time: O(n)
# Space: O(1)
def convert_to_int(s):
    if not s:
        return None

    result = 0
    is_negative = False

    if s[0] == "-":
        is_negative = True
        s = s[1:]

    ascii_zero = ord('0')

    for ch in s:
        if not ch.isdigit():
            return None
        result = result * 10 + ord(ch) - ascii_zero
    return -result if is_negative else result

print(convert_to_int('-105') + 1)