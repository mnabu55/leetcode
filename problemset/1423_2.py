from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        ans = win = 0
        for i in range(-k, k):
            win += cardPoints[i]
            if i >= 0:
                win -= cardPoints[i - k]
            ans = max(win, ans)
        return ans


ins = Solution()
print(ins.maxScore([1,2,3,4,5,6,1], 3))