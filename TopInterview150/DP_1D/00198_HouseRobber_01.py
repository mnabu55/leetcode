from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return max(nums)
        
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        return dp[n-1]


if __name__ == "__main__":
    solution = Solution()
    
    nums = [1, 2, 3, 1]
    assert solution.rob(nums) == 4

    nums = [2, 7, 9, 3, 1]
    assert solution.rob(nums) == 12

    nums = [2, 1, 1, 2]
    assert solution.rob(nums) == 4
