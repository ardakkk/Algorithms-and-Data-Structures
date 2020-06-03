# Time: O(n)
# Space: O(n)
def square_numbers(nums):
    negative_stacks = []

    result = []
    for n in nums:
        if n < 0:
            negative_stacks.append(n)
            continue

        while len(negative_stacks) and -negative_stacks[-1] <= n:
            result.append(negative_stacks.pop() ** 2)
        result.append(n**2)

    while len(negative_stacks) > 0:
        result.append(negative_stacks.pop()**2)

    return result

print(square_numbers([-5, -3, -1, 0, 1, 4, 5]))