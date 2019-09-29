# Time: O(n) | Space: O(n)
# def caesarCipherEncryptor(string, key):
#     newLetters = []
#     newKey = key % 26
#
#     for letter in string:
#         newLetters.append(getNewLetter(letter, newKey))
#     return "".join(newLetters)
#
# def getNewLetter(letter, key):
#     newLetterCode = ord(letter) + key
#     return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 122)

# Time: O(n) | Space: O(n)
def caesarCipherEncryptor(string, key):
    newLetters = []
    newKey = key % 26
    alphabet = list("abcdefghijklmopqrstuvwxyz")
    for letter in string:
        newLetters.append(getNewLetter(letter, newKey, alphabet))
    return "".join(newLetters)

def getNewLetter(letter, key, alphabet):
    newLetterCode = alphabet.index(letter) + key
    return alphabet(newLetterCode) if newLetterCode <= 25 else alphabet[-1 + newLetterCode % 25]