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

# Time: O(n log n)
# Space: O(n)
class Solution2:
    def minMeetingRooms(self, intervals):
        start = []
        end = []

        for i in intervals:
            start.append(i[0])
            end.append(i[1])

        start.sort()
        end.sort()

        s = 0
        e = 0

        numRooms = 0
        available = 0

        while s < len(start):
            if start[s] < end[e]:
                if available:
                    available -= 1
                else:
                    numRooms += 1
                s += 1
            else:
                available += 1
                e += 1

        return numRooms
