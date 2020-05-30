# Time: O(n)
# Space: O(1)
def findThreeLargestNumbers(array):
    threeLargestNumbers = [None, None, None]

    for num in array:
        updateLargest(threeLargestNumbers, num)

    return threeLargestNumbers

def updateLargest(threeLargest, num):
    if threeLargest[2] is None or num > threeLargest[2]:
        shiftAndUpdate(threeLargest, num, 2) #TODO
    elif threeLargest[1] is None or num > threeLargest[1]:
        shiftAndUpdate(threeLargest, num, 1)
    elif threeLargest[0] is None or num > threeLargest[0]:
        shiftAndUpdate(threeLargest, num, 0)

def shiftAndUpdate(array, num, idx):
    # [0, 1, 2]
    # [y, z, num]
    # for i in range(0, 2 + 1)
    # if i == 2:

    for i in range(idx + 1):
        if i == idx:
            array[i] = num
        else:
            array[i] = array[i + 1]