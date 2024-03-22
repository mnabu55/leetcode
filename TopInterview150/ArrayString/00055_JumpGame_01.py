from typing import List


class Solution:
    def canJump_solution1(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return True
        
        longest = nums[0]
        for i in range(1, n):
            if i > longest:
                return False
            longest = max(longest, i + nums[i])
            if longest >= n - 1:
                return True

        return True


    def canJump(self, nums: List[int]) -> bool:
        remaining_gas = 0
        
        for gas in nums:
            if remaining_gas < 0:
                return False
            elif gas > remaining_gas:
                remaining_gas = gas
            remaining_gas -= 1

        return True


if __name__ == '__main__':
    solution = Solution()

    nums = [2,3,1,1,4]
    expected = True
    assert solution.canJump(nums) == expected

    nums = [3,2,1,0,4]
    expected = False
    assert solution.canJump(nums) == expected
