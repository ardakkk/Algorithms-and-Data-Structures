# Time: O(n^2) | Space: O(n)
# def isPalindrome(string):
#     reversedString = ""
#
#     for i in reversed(range(len(string))):
#         reversedString += string[i]
#     return string == reversedString

# Time: O(n) | Space: O(n)
# def isPlaindrome(string):
#     reversedChars = []
#
#     for i in reversed(range(len(string))):
#         reversedChars.append(string[i])
#     return string == "".join(reversedChars)

# Time: O(n) | Space: O(n)
# def isPlaindrome(string, i = 0):
#     j = len(string) - 1 - i
#     return True if i >= j else string[i] == string[j] and isPlaindrome(string, i + 1)

# Time: O(n) | Space: O(n)
# def isPalindrome(string, i = 0):
#     j = len(string) - 1 - i
#
#     if i >= j:
#         return True
#     if string[i] != string[j]:
#         return False
#
#     return isPalindrome(string, i + 1)

# Time: O(n) | Space: O(1)
def isPalindrome(string):
    leftIdx = 0
    rightIdx = len(string) - 1

    while leftIdx < rightIdx:
        if string[leftIdx] != string[rightIdx]:
            return False

        leftIdx += 1
        rightIdx -= 1

    return True

print(isPalindrome('abcdcba'))
