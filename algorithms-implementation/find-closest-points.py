import heapq

def calcDistance(p):
    return p[0]*p[0] + p[1]*p[1]

# Brute-force solution
# Time: O(nlong)
# Space: O(1)
def findClosestPoints(points, k):
    points = sorted(points, key=lambda x: calcDistance(x))
    return points[:k]

# Using heap data structures
# Time: O(k logn)
# Space: O(n)
def findClosestPoints(points, k):
    # (distance, object)
    data = []
    for p in points:
        data.append((calcDistance(p), p))
    heapq.heapify(data)

    result = []
    for i in range(k):
        result.append(heapq.heappop(data)[1])
    return result


print(findClosestPoints([[1, 1], [3, 3], [2, 2], [4, 4], [-1, -1]], 3))
