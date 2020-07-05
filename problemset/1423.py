from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        size = len(cardPoints) - k
        minSubArraySum = float('inf')
        j = curr = 0

        for i, v in enumerate(cardPoints):
            curr += v
            if i - j + 1 > size:
                curr -= cardPoints[j]
                j += 1
            if i - j + 1 == size:
                minSubArraySum = min(minSubArraySum, curr)

        return sum(cardPoints) - minSubArraySum


ins = Solution()
assert ins.maxScore([1,2,3,4,5,6,1], 3) == 12, "ng: case [1,2,3,4,5,6,1]"
