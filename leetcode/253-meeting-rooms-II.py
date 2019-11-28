from heapq import heappush, heappop

# Time: O(n log n) Our Solution uses a Sorting Algorithm.
# Space: O(n) Worst case our Heap is size of N.
class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0
        priorty_queque = []

        intervals.sort(key=lambda interval: interval.start)

        heappush(priorty_queque, intervals[0].end)

        for i in range(1, len(intervals)):
            current_interval = intervals[i]
            earliest_end = priorty_queque[0]

            if current_interval.start >= earliest_end:
                heappush(priorty_queque, current_interval.end)
                heappop(priorty_queque)
            else:
                heappush(priorty_queque, current_interval.end)

        return len(priorty_queque)

solution = Solution()
print(solution.minMeetingRooms([(0, 30), (5, 10), (15, 20)]))

