'''
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
'''

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        nums.sort()
        number_dict = {}
        for v in nums:
            if v not in number_dict:
                number_dict[v] = 1
            else:
                number_dict[v] += 1
        single_number_list = [k for k, v in number_dict.items() if v <= 1]
        return single_number_list


ins = Solution()
assert ins.singleNumber([1,2,1,3,2,5]) == [3,5], "case 1 ng"
