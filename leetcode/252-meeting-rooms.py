# Given an array of meeting time intervals consisting of start and end
# canAttendMeetings([[0, 30], [5, 10], [15, 20]]) --> False
# canAttendMeetings([[2, 4], [7, 10]]) --> True

class Solution:
    def canAttendMeetings(self, intervals):
        starts = []
        ends = []

        for sub_list in intervals:
            starts.append(sub_list[0])
            ends.append(sub_list[1])

        starts = sorted(starts)
        ends = sorted(ends)

        for i in range(len(starts) - 1):
            if starts[i + 1] < ends[i]:
                return False

        return True

solution = Solution()

print(solution.canAttendMeetings([[0, 30], [5, 10], [15, 20]])) # False
print(solution.canAttendMeetings([[2, 4], [7, 10]])) # True