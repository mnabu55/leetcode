from typing import List

# https://leetcode.com/problems/permutations/
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

# Example 1:

# Input: nums = [1,2,3]
# Output:


class Solution:
    # Backtrack solution
    def permute_backtrack(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(first=0):
            if first == len(nums) - 1:
                result.append(nums[:])
                return

            for i in range(first, len(nums)):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        backtrack()
        return result

    # Iterative solution
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        if len(nums) <= 1:
            return [nums]
        for perm in self.permute(nums[1:]):
            for i in range(len(nums)):
                result.append(perm[:i] + nums[0:1] + perm[i:])

        return result


if __name__ == "__main__":
    nums = [1, 2, 3]
    solution = Solution()
    result = solution.permute(nums)
    print(result)
# Output:
#    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
