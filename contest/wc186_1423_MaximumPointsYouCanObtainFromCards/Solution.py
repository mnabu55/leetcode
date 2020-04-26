from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        score = 0
        idx_left = 0
        idx_right = len(cardPoints) - 1
        take_count = 0

        while (idx_left < idx_right) and (take_count < k):
            if cardPoints[idx_left] >= cardPoints[idx_right]:
                print("left large, plus {}".format(cardPoints[idx_left]))
                score += cardPoints[idx_left]
                idx_left += 1
            else:
                print("rightl large, plus {}".format(cardPoints[idx_right]))
                score += cardPoints[idx_right]
                idx_right -= 1
            take_count += 1

        print(score)
        return score

sol = Solution()
assert sol.maxScore([1,2,3,4,5,6,1], 3) == 12, "ERROR 1"
assert sol.maxScore([100,40,17,9,73,75], 3) == 248, "ERROR 2"
