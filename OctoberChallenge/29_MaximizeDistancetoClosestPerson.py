'''
You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).
There is at least one empty seat, and at least one person sitting.
Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.
Return that maximum distance to the closest person.

Example 1:
Input: seats = [1,0,0,0,1,0,1]
Output: 2
Explanation:
If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.

Example 2:
Input: seats = [1,0,0,0]
Output: 3
Explanation:
If Alex sits in the last seat (i.e. seats[3]), the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.

Example 3:
Input: seats = [0,1]
Output: 1

Constraints:
2 <= seats.length <= 2 * 104
seats[i] is 0 or 1.
At least one seat is empty.
At least one seat is occupied.
'''

from typing import List
import math


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_distance = 0
        i = 0

        while i < len(seats):
            if seats[i] == 1:
                i += 1
                continue
            j = i + 1
            while j < len(seats) and seats[j] == 0:
                j += 1

            len_empty_range = j - i
            if i == 0 or j == len(seats):
                distance = len_empty_range
            else:
                distance = math.ceil(len_empty_range / 2)
            max_distance = max(max_distance, distance)

            i = j + 1

        return max_distance


solution = Solution()
assert solution.maxDistToClosest([1,0,0,0,1,0,1]) == 2, "case01,ng"
assert solution.maxDistToClosest([1,0,0,0]) == 3, "case02,ng"
assert solution.maxDistToClosest([0,1]) == 1, "case03,ng"
assert solution.maxDistToClosest([1,0,0,1]) == 1, "case04,ng"
assert solution.maxDistToClosest([0,0,1]) == 2, "case05,ng"
