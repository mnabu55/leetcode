'''
Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.
'''

from typing import List

class Solution:
    def maxScore(self, s: str) -> int:
        length = len(s)
        score_list = []

        for i in range(1, length):
            count_zero = s.count('0', 0, i)
            count_one = s.count('1', i, length)
            score_list.append(count_zero + count_one)

        return max(score_list)


sol = Solution()
assert sol.maxScore("011101") == 5, "ERROR: 011101"
assert sol.maxScore("00111") == 5, "ERROR: 00111"
assert sol.maxScore("1111") == 3, "ERROR: 1111"
