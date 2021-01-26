'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
1 <= n <= 45
'''


class Solution:
    memo = {}

    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        if n in self.memo:
            return self.memo[n]
        result = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        self.memo[n] = result
        return result


solution = Solution()
assert solution.climbStairs(2) == 2, "case01,ng"
assert solution.climbStairs(3) == 3, "case02,ng"
assert solution.climbStairs(4) == 5, "case03,ng"
assert solution.climbStairs(5) == 8, "case04,ng"
