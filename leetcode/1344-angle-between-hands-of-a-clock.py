# Time: O(1)
# Space: O(1)
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        if (hour == 12):
            hour = 0
        if (minutes == 60):
            minutes = 0

        hour_angle = (360 / (12 * 60)) * (hour * 60 + minutes)
        min_angle = 360 / 60.0 * minutes
        angle = abs(hour_angle - min_angle)

        return min(angle, 360 - angle)