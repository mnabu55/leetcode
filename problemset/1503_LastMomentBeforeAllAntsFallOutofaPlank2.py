from typing import List


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        left_max = max(left) if left else 0
        right_max = (n - min(right)) if right else 0
        return max(left_max, right_max)


ins = Solution()
assert ins.getLastMoment(4, [4,3], [0,1]) == 4, "case1 ng"
assert ins.getLastMoment(7, [], [0,1,2,3,4,5,6,7]) == 7, "case2 ng"
assert ins.getLastMoment(7, [0,1,2,3,4,5,6,7], []) == 7, "case3 ng"
assert ins.getLastMoment(9, [5], [4]) == 5, "case4 ng"
