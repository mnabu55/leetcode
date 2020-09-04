'''
Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.
Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

Example 1:
Input: [1,2,3,4]

Output: "23:41"
Example 2:

Input: [5,5,5,5]
Output: ""

Note:
A.length == 4
0 <= A[i] <= 9
'''

from typing import List
from itertools import permutations


class Solution:
    def listExcludedIndices(self, data, indices=[]):
        return [x for i, x in enumerate(data) if i not in indices]

    def largestTimeFromDigits(self, A: List[int]) -> str:
        # A Python program to print all
        # permutations using library function

        # Get all permutations of [1, 2, 3]
        perm = permutations(A)

        max_time = -1
        # Print the obtained permutations
        for word in list(perm):
            time_ = int("".join([str(s) for s in word]))
            if time_ <= 2359:
                max_time = max(max_time, time_)

        time_s = str(max_time)
        if max_time < 0:
            result = ""
        elif max_time == 0:
            result = "00:00"
        elif max_time <= 2359:
            tmp = ["0", "0", "0", "0"]
            for i in range(4):
                tmp[3 - i] = str(max_time % 10)
                max_time //= 10
                result = "".join([s for s in tmp[:2]]) + ":" + "".join([s for s in tmp[2:]])
        return result


solution = Solution()
assert solution.largestTimeFromDigits([1,2,3,4]) == "23:41", "case01,ng"
assert solution.largestTimeFromDigits([5,5,5,5]) == "", "case02,ng"
assert solution.largestTimeFromDigits([0,0,0,0]) == "00:00", "case03,ng"
