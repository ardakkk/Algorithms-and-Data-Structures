"""
Sum of Squares

Given a number n, find the least number of squares needed to sum up to the number.

Here's an example and some starting code:
"""

# Time: O(n * sqrt(n))
# Space: O()
def square_sum(n):
    squares = []

    i = 1
    while i * i <= n:          # sqrt(n)
        squares.append(i * i)
        i += 1

    min_sums = [n] * (n+1)
    min_sums[0] = 0

    for idx in range(len(min_sums)):
        for s in squares:
            if idx + s < len(min_sums):
                min_sums[idx+s] = min(min_sums[idx+s], min_sums[idx] + 1)

    return min_sums[-1]

print(square_sum(13))
# min sum is 3^2 + 2^2
# 2

print(square_sum(9))
# min sum is 3^3
# 1