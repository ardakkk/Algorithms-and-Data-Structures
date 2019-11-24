# Time: O(N log N) Our Solution uses a Sorting Algorithm.
# Space: O(1) We sort the Input Array in place.
class Solution:
    def merge(self, intervals):
        if not intervals:
            return []

        intervals.sort(key=lambda interval: interval[0])  # O(N log N)

        res = [intervals[0]]

        for current_interval in intervals:
            last_interval = res[-1]

            # if there is an overlap
            if current_interval[0] <= last_interval[1]:
                last_interval[1] = max(current_interval[1], last_interval[1])
            else:
                res.append(current_interval)

        return res

solution = Solution()
print(solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))

