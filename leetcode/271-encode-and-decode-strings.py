# Example
# encoded_string = encode(["kevin", "is", "great"])
#                  "5/kevin2/is5/great"

# decoded_array = decode("5/kevin2/is5/great")
#                 ["kevin", "is", "great"]

# Time: O(n) For encode and decode | Space: O(1)
class Solution:
    def encode(self, strs):
        encoded = ""
        for word in strs:
            length = len(word)
            encoded += strs(length) + "/" + word

        return encoded

    def decode(self, str):
        pos = 0
        decoded = []

        while pos < len(str):
            slash_pos = str.index("/", pos)
            length = int(str[slash_pos - 1])
            pos = slash_pos + 1

            decoded.append(str[pos: pos + length])
            pos += length

        return decoded


print(Solution.decode('5/kevin2/is5/great'))
