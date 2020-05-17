# Time: O(n) | Space: O(1)
def validateSubsequence(array, sequence):
    seqIdx = 0
    arrIdx = 0

    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1

    return seqIdx == len(sequence)

# Time: O(n) | Space: O(1)
def validateSubsequence2(array, sequence):
    seqIdx = 0

    for value in array:
        if seqIdx == len(sequence):
            return True
        if sequence[seqIdx] == value:
            seqIdx += 1

    return seqIdx == len(sequence)

print(validateSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))