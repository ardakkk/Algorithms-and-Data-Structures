# Time: O(n logn) Using sorting algorithms
# Space: 0(1) We sort the input array in place
class Solution:
    def eraseOverlapIntervals(self, intervals):
        if not intervals:
            return 0

        erase_count = 0

        intervals.sort(key=lambda interval: interval[0])

        previous_interval_end = intervals[0][1]

        for i in range(1, len(intervals)):
            interval = intervals[i]
            start_interval = interval[0]
            end_interval = interval[1]

            if start_interval < previous_interval_end:
                erase_count += 1
                previous_interval_end = min(previous_interval_end, end_interval)

            else:
                previous_interval_end = end_interval

        return erase_count
