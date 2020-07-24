'''
Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.

Example 1:
Input: hour = 12, minutes = 30
Output: 165

Example 2:
Input: hour = 3, minutes = 30
Output: 75

Example 3:
Input: hour = 3, minutes = 15
Output: 7.5

Example 4:
Input: hour = 4, minutes = 50
Output: 155

Example 5:
Input: hour = 12, minutes = 0
Output: 0

Constraints:
1 <= hour <= 12
0 <= minutes <= 59
Answers within 10^-5 of the actual value will be accepted as correct.
'''


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hourangle = (hour % 12) * 30 + minutes * 0.5
        minuteangle = minutes * 6
        if minuteangle >= hourangle:
            angle = minuteangle - hourangle
        else:
            angle = hourangle - minuteangle
        if angle > 180:
            angle = 360 - angle
        return angle


ins = Solution()
assert ins.angleClock(12, 30) == 165, "case 1 ng"
assert ins.angleClock(3, 30) == 75, "case 2 ng"
assert ins.angleClock(3, 15) == 7.5, "case 3 ng"
assert ins.angleClock(4, 50) == 155, "case 4 ng"
assert ins.angleClock(12, 0) == 0, "case 5 ng"
