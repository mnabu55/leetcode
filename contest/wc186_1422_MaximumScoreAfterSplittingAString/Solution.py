from typing import List

class Solution:
    def maxScore(self, s: str) -> int:
        len_s = len(s)
        max_score = 0

        for i in range(1, len(s)):
            count_zero = s.count('0', 0, i)
            count_one = s.count('1', i, len_s)
            sum_zero_one = count_zero + count_one

            if sum_zero_one > max_score:
                max_score = sum_zero_one

        return max_score


sol = Solution()
assert sol.maxScore("011101") == 5, "ERROR: 011101"
assert sol.maxScore("00111") == 5, "ERROR: 00111"
assert sol.maxScore("1111") == 3, "ERROR: 1111"
