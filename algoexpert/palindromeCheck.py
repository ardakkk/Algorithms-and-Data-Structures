# Time: O(n^2) | Space: O(n)
# def isPalindrome(string):
#     reversedString = ""
#
#     for i in reversed(range(len(string))):
#         reversedString += string[i]
#         return string == reversedString

# Time: O(n) | Space: O(n)
# def isPlaindrome(string):
#     reversedChars = []
#
#     for i in reversed(range(len(string))):
#         reversedChars.append(string[i])
#     return string == "".join(reversedChars)

# Time: O(n) | Space: O(n)
def isPlaindrome(string, i = 0):
    j = len(string) - 1 - i
    return True if i >= j else string[i] == string[j] and isPlaindrome(string, i + 1)

print(isPlaindrome("abcdcba"))