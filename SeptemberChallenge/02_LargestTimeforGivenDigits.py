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


class Solution:
    def listExcludedIndices(self, data, indices=[]):
        return [x for i, x in enumerate(data) if i not in indices]

    def largestTimeFromDigits(self, A: List[int]) -> str:
        result = []
        for i in range(len(A)):
            for j in range(len(A) - 1):
                for k in range(len(A) - 2):
                    jData = self.listExcludedIndices(A, [i])
                    kData = self.listExcludedIndices(jData, [j])
                    result.append([A[i], jData[j], kData[k]])
        print(result)
        return result


solution = Solution()
assert solution.largestTimeFromDigits([1,2,3,4]) == "23:41", "case01,ng"
