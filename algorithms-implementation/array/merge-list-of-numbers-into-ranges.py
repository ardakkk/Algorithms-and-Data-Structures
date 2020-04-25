def makeranges(low, high):
    return str(low) + '-' + str(high)

# Time: O(n)
# Space: O(1)
def findRanges(nums):
    if not nums:
        return []
    ranges = []
    low = nums[0]
    high = nums[0]

    for n in nums:
        if high + 1 < n:
            ranges.append(makeranges(low, high))
            low = high = n
        else:
            high = n
    ranges.append(makeranges(low, high))
    return ranges

print(findRanges([0, 1, 2, 3, 5, 7, 8, 9, 9, 10, 11, 15]))