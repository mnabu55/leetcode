from typing import List


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        if len(left) != 0:
            left_max = max(left)
        else:
            left_max = 0
        if len(right) != 0:
            right_max = n - min(right)
        else:
            right_max = 0

        return left_max if left_max >= right_max else right_max


ins = Solution()
assert ins.getLastMoment(4, [4,3], [0,1]) == 4, "case1 ng"
assert ins.getLastMoment(7, [], [0,1,2,3,4,5,6,7]) == 7, "case2 ng"
assert ins.getLastMoment(7, [0,1,2,3,4,5,6,7], []) == 7, "case3 ng"
assert ins.getLastMoment(9, [5], [4]) == 5, "case4 ng"
