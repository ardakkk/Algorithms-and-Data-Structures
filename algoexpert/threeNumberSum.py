# Time: 0(n^2) | Space: O(n)
def threeNumberSum(array, target_sum):
    array.sort()
    triplets = []
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1

        while left < right:
            current_sum = array[i] = array[left] + array[right]
            if current_sum == target_sum:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif current_sum < target_sum:
                left += 1
            elif current_sum > target_sum:
                right -= 1
    return triplets

print(threeNumberSum([-1, 0, 1, 2, -1, -4], 0))