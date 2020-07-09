'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''


from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3:
            return []

        nums.sort()

        result = []
        for i in range(n-2):
            j = i + 1
            k = n - 1
            while j < k:
                sum3 = nums[i] + nums[j] + nums[k]
                if sum3 == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif sum3 > 0:
                    k -= 1
                else:
                    j += 1

        return list(map(list, set(map(tuple, result))))


ins = Solution()
print(ins.threeSum([-1, 0, 1, 2, -1, -4]))
