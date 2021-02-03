'''
Given an array nums of 0s and 1s and an integer k, return True if all 1's are at least k places away from each other, otherwise return False.

Example 1:
Input: nums = [1,0,0,0,1,0,0,1], k = 2
Output: true
Explanation: Each of the 1s are at least 2 places away from each other.

Example 2:
Input: nums = [1,0,0,1,0,1], k = 2
Output: false
Explanation: The second 1 and third 1 are only one apart from each other.

Example 3:
Input: nums = [1,1,1,1,1], k = 0
Output: true

Example 4:
Input: nums = [0,1,0,1], k = 1
Output: true

Constraints:
1 <= nums.length <= 105
0 <= k <= nums.length
nums[i] is 0 or 1
'''
from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        nums_len = len(nums)

        # search first 1
        first_pos = 0
        while first_pos < nums_len and nums[first_pos] == 0:
            first_pos += 1

        # now 1
        i = first_pos + 1
        while i < nums_len:
            length = 0
            while i < nums_len and nums[i] == 0:
                length += 1
                i += 1
            if length < k and i < nums_len:
                return False
            i += 1
        return True


solution = Solution()
assert solution.kLengthApart([1,0,0,0,1,0,0,1], 2) == True, "case01,ng"
assert solution.kLengthApart([1,0,0,1,0,1], 2) == False, "case02,ng"
assert solution.kLengthApart([1,1,1,1,1], 0) == True, "case03,ng"
assert solution.kLengthApart([0, 1, 0, 1], 1) == True, "case04,ng"
assert solution.kLengthApart([0, 0, 0], 2) == True, "case05,ng"
assert solution.kLengthApart([1,0,0,0,1,0,0,1,0], 2) == True, "case06,ng"