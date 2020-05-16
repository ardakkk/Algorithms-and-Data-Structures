class Solution:
    def calcDistance(self, p):
        return p[0] * p[0] + p[1] * p[1]

    # Time: O(klogn)
    # Space: O(n)
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        data = []
        for p in points:
            data.append((self.calcDistance(p), p))
        heapq.heapify(data)

        result = []
        for i in range(K):
            result.append(heapq.heappop(data)[1])
        return result
