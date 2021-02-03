'''
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements that appear twice in this array.
Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
'''


from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums_dict = {}
        for n in nums:
            if n not in nums_dict:
                nums_dict[n] = 1
            else:
                nums_dict[n] += 1

        return [k for k, v in nums_dict.items() if v >= 2]


solution = Solution()
assert solution.findDuplicates([1,1,2,2,3,4]) == [1,2], "NG: case 1"
