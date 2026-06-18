"""
Given two numbers, hour and minutes, return the smaller angle (in degrees)
formed between the hour and the minute hand.
"""


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        TOTAL_HOURS = 12
        MINUTES_PER_HOUR = 60
        TOTAL_DEGREES = 360
        DEGREE_PER_HOUR = TOTAL_DEGREES / TOTAL_HOURS # 30°
        DEGREE_PER_MINUTE = DEGREE_PER_HOUR / MINUTES_PER_HOUR # 0.5°
        MINUTE_HAND_DEGREE_PER_MINUTE = TOTAL_DEGREES / MINUTES_PER_HOUR # 6°

        # angle of hour hand
        hour_angle = DEGREE_PER_HOUR * hour
        # plus slight angle of hour hand within an hour due to minutes
        hour_angle += DEGREE_PER_MINUTE * minutes
        # angle of minute hand
        minute_angle = MINUTE_HAND_DEGREE_PER_MINUTE * minutes

        # clock angle is the diff between hour_angle - minute_angle
        clock_angle = abs(hour_angle - minute_angle)
        # return the smaller angle between the two hands
        return min(clock_angle, 360 - clock_angle)


def main():
    while True:
        try:
            line = input()
            hour = int(line)
            line = input()
            minutes = int(line)

            ret = Solution().angleClock(hour, minutes)

            print(ret)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
