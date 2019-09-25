# Time: O(nLog(n) + mLog(m)) | Space: O(1)

def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayOne.sort()
    idxOne = 0
    idxTwo = 0
    smallest = float("inf")
    current = float("inf")
    smallestPair = []

    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]

        if firstNum < secondNum:
            current = secondNum - firstNum
            idxOne += 1
        elif secondNum < firstNum:
            current = firstNum - secondNum
            idxTwo += 1
        else:
            return [firstNum, secondNum]

        if smallest > current:
            smallest = current
            smallestPair = [firstNum, secondNum]
        return smallestPair

print(smallestDifference([1, 45, 23, 56], [26, 3, 4, 7]))